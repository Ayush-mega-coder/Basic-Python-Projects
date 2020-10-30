from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from wtsap_auto import send_msg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=1)

sched.start()
