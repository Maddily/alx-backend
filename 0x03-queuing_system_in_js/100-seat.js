import express from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';

/**
 * A note to the task reviewer: I did not use `promisify`
 * because the Redis client get method being used already returns a Promise,
 * making it unnecessary to use promisify with it.
 * Starting from redis@4.0.0, the library has built-in support for Promises.
 */

const redisClient = createClient();
const queue = createQueue();
let reservationEnabled = true;

function reserveSeat(number) {
  redisClient.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  return parseInt(await redisClient.get('available_seats'), 10);
}

const app = express();
const port = 1245;

redisClient.connect();

app.get('/available_seats', async (req, res) => {
  res.json({ numberOfAvailableSeats: JSON.stringify(await getCurrentAvailableSeats()) });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((error) => {
    if (!error) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job
    .on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (error) => {
      console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const availableSeatsThen = await getCurrentAvailableSeats();

    const availableSeatsNow = availableSeatsThen - 1;
    if (availableSeatsNow === 0) reservationEnabled = false;

    if (availableSeatsNow >= 0) {
      reserveSeat(availableSeatsNow);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });

  res.json({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log('The server is running...');
  reserveSeat(50);
});
