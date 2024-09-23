export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      .on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      });

    job.save();
  }
}
