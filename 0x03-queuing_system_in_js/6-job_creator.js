import { createQueue } from 'kue';

const jobData = {
  phoneNumber: '01000000000',
  message: 'Hello, this is a test!',
};

const queue = createQueue();
const job = queue.create('push_notification_code', jobData).save((error) => {
  if (error) {
    console.error(`Error creating job: ${error}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
