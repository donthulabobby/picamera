from picamera import PiCamera
import time
import datetime


print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

print "Hour is: " , datetime.datetime.now().strftime('%H')
print "Minute is: " , datetime.datetime.now().strftime('%M')



print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")

todayDateTime = datetime.date.today()
dateTimeNow = datetime.datetime.now()
month = todayDateTime.strftime("%B")
day = todayDateTime.strftime("%d")
hour = dateTimeNow.strftime('%H')
minute = dateTimeNow.strftime('%M')
print month + day + hour + minute

timeInSecsToRecord = ((60 - int(minute)) * 60)
print timeInSecsToRecord
#time.sleep(10)



camera = PiCamera()

camera.resolution = (1280, 720)
while True:
#for i in range(1,11):
  todayDateTime = datetime.date.today()
  dateTimeNow = datetime.datetime.now()
  month = todayDateTime.strftime("%B")
  day = todayDateTime.strftime("%d")
  hour = dateTimeNow.strftime('%H')
  minute = dateTimeNow.strftime('%M')
  print month + day + hour + minute

  timeInSecsToRecord = ((60 - int(minute)) * 60)
  print timeInSecsToRecord
  camera.start_preview()
  camera.start_recording("/home/pi/Desktop/testVideoDir/" + month + "/" + day + "/"+ hour + "-" + minute + ".h264")
  camera.wait_recording(timeInSecsToRecord)
  camera.stop_recording()
  camera.stop_preview()
