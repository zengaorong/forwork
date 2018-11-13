import datetime
import time


starttime = datetime.datetime.now()
print starttime

isrun = True
hour = 0
secode = 50
minutes = 1
times = hour*60*60 + minutes*60 + minutes

while isrun:
    endtime = datetime.datetime.now()
    if (endtime - starttime).seconds > times:
        print (endtime - starttime).seconds
        print "is time"
        isrun =  False
    else:
        time.sleep(0.5)