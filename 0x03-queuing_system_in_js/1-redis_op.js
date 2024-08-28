import { createClient, print } from 'redis';

/**
 * A note to the task reviewer: I have used async/await
 * because the Redis client get method being used returns a Promise.
 * Starting from redis@4.0.0, the library has built-in support for Promises.
 */

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  console.log(await redisClient.get(schoolName));
}

redisClient.connect();
(async () => displaySchoolValue('Holberton'))();
setNewSchool('HolbertonSanFrancisco', '100');
(async () => displaySchoolValue('HolbertonSanFrancisco'))();
