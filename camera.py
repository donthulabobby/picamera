import time
import datetime
import os
import logging
import traceback
from picamera import PiCamera

logging.basicConfig(filename='/var/log/picamera.log',level=logging.DEBUG)
camera = PiCamera()
camera.resolution = (1920, 1080)

while True:
  try:
    todayDateTime = datetime.date.today()
    dateTimeNow = datetime.datetime.now()
    month = todayDateTime.strftime("%B")
    day = todayDateTime.strftime("%d")
    hour = dateTimeNow.strftime('%H')
    minute = dateTimeNow.strftime('%M')
    timeInSecsToRecord = ((60 - int(minute)) * 60)
    directory = "/home/pi/Desktop/picamRecordings/" + month + "/" + day + "/"
    if not os.path.exists(directory):
      os.makedirs(directory)
    filename = hour + "h" + "-" + minute + "m" + ".h264"
    videoFilePath = directory + filename
    logging.info(videoFilePath + ". Recording Time in Seconds: " + timeInSecsToRecord)
    camera.start_recording(videoFilePath)
    camera.wait_recording(timeInSecsToRecord)
    camera.stop_recording()
  except Exception as e:
  	logging.error("Error happened while recording: " + videoFilePath)
    logging.error(traceback.format_exc())
    # Logs the error appropriately. 
