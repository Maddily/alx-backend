import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';
import { expect } from 'chai';

describe('createPushNotificationsJobs', function () {
  let queue;

  beforeEach(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('throws an error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('Not an array', queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should successfully enqueue jobs', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });

  it('should enqueue the jobs with their data intact', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780')
    expect(queue.testMode.jobs[0].data.message).to.equal('This is the code 1234 to verify your account')
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3')

    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4153518781')
    expect(queue.testMode.jobs[1].data.message).to.equal('This is the code 4562 to verify your account')
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3')
  });
});
