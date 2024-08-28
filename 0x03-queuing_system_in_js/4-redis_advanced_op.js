import { createClient, print } from 'redis';

/**
 * A note to the task reviewer: I have used async/await
 * because the Redis client hGetAll method being used returns a Promise.
 * Starting from redis@4.0.0, the library has built-in support for Promises.
 */

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redisClient.on('connect', async () => {
  console.log('Redis client connected to the server');

  redisClient.hSet('HolbertonSchools', 'Portland', 50, print);
  redisClient.hSet('HolbertonSchools', 'Seattle', 80, print);
  redisClient.hSet('HolbertonSchools', 'New York', 20, print);
  redisClient.hSet('HolbertonSchools', 'Bogota', 20, print);
  redisClient.hSet('HolbertonSchools', 'Cali', 40, print);
  redisClient.hSet('HolbertonSchools', 'Paris', 2, print);

  console.log(await redisClient.hGetAll('HolbertonSchools'));
});

redisClient.connect();
