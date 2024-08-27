import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');

  redisClient.hSet('HolbertonSchools', 'Portland', 50, print);
  redisClient.hSet('HolbertonSchools', 'Seattle', 80, print);
  redisClient.hSet('HolbertonSchools', 'New York', 20, print);
  redisClient.hSet('HolbertonSchools', 'Bogota', 20, print);
  redisClient.hSet('HolbertonSchools', 'Cali', 40, print);
  redisClient.hSet('HolbertonSchools', 'Paris', 2, print);

  redisClient.hGetAll('HolbertonSchools', (_, res) => {
    console.log(res);
  });
});

redisClient.connect();
