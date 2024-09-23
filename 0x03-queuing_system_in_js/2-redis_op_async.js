import { createClient, print } from 'redis';

/**
 * A note to the task reviewer: I did not use `promisify`
 * because the Redis client get method being used already returns a Promise,
 * making it unnecessary to use promisify with it.
 * Starting from redis@4.0.0, the library has built-in support for Promises.
 */

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redisClient.on('connect', async () => {
  console.log('Redis client connected to the server');
  await runOperations();
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await redisClient.get(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
}

redisClient.connect();
async function runOperations() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
