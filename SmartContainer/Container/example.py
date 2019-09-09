import schedule
import time, traceback
from apscheduler.schedulers.background import BackgroundScheduler  #다수수행
#단일수행은 BlockingScheduler
from apscheduler.jobstores.base import JobLookupError
from croniter import croniter
from datetime import datetime
import threading


#방법1 schdule 사용
#def job():
#    print("I'm working...", "| [time] ",
#          str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
#schedule.every(5).seconds.do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)





#방법2 람다 사용
#def every(delay, task):
#  next_time = time.time() + delay
#  while True:
#    time.sleep(max(0, next_time - time.time()))
#    try:
#      task()
#    except Exception:
#      traceback.print_exc()
#    next_time += (time.time() - next_time) // delay * delay + delay

#def job2():
#    print("I'm working...", "| [time] ",
#            str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
#threading.Thread(target=lambda: every(5, job2)).start()














#여기서부턴 다른거 해보던거
#now = time.localtime()
#print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

#base = datetime(2019, 8, 21, 15, 45)       #기준시간(시작시간)
#iter = croniter('*/5 * * * *', now)    #매 5분마다 / 크로니터사용
#print(iter.get_next(datetime))
#print(iter.get_next(datetime))


#def job():
#    print(iter.get_next(datetime))
#    print("I'm working...", "| [time] " , str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
#sched = BackgroundScheduler()
#sched.start()
#sched.add_job(job, 'cron', minute='*/1', id="test_1")

#while True:
#    print(iter.get_next(datetime))
#    time.sleep(1)




