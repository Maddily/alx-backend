import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

(async () => await redisClient.connect())();
(async () => {
  await redisClient.subscribe('holberton school channel', async (message) => {
    console.log(message);

    if (message === 'KILL_SERVER') {
      await redisClient.unsubscribe('holberton school channel');
      await redisClient.quit();
    }
  });
})();
