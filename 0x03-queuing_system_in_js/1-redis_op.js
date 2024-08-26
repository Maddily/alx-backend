import { createClient, print } from 'redis';

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

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_, value) => {
    console.log(value);
  });
}

redisClient.connect();
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
