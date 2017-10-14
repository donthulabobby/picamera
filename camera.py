import time
import datetime
import os
import logging
import traceback
import sqlite3 as lite
from picamera import PiCamera

logging.basicConfig(filename='/var/log/picamera.log',level=logging.DEBUG)
camera = PiCamera()
camera.resolution = (1296, 972)
videoRecordingsDir = "/var/piCamRecordings/"
historyNumDaysForRecordings = 60
location = "/var/pi/picam.db"
table_name = "pi_videos"
conn = lite.connect(location)
cur = conn.cursor()


def insertVideoFilePath( filePath, cursor, connection ):
  sql = "insert into pi_videos(file) values ('hello')"
  cursor.execute(sql)
  connection.commit()


while True:
  try:
    todayDateTime = datetime.date.today()
    dateTimeNow = datetime.datetime.now()
    month = todayDateTime.strftime("%B")
    day = todayDateTime.strftime("%d")
    hour = dateTimeNow.strftime('%H')
    minute = dateTimeNow.strftime('%M')
    timeInSecsToRecord = ((60 - int(minute)) * 60)
    directory = videoRecordingsDir + month + "/" + day + "/"
    if not os.path.exists(directory):
      os.makedirs(directory)
    filename = hour + "h" + "-" + minute + "m" + ".h264"
    videoFilePath = directory + filename
    insertVideoFilePath(videoFilePath, cur, conn)
    logging.info(videoFilePath + ". Recording Time in Seconds: " + str(timeInSecsToRecord))
    camera.start_recording(videoFilePath)
    camera.wait_recording(timeInSecsToRecord)
    camera.stop_recording()
  except Exception as e:
    logging.error("Error happened while recording: " + videoFilePath)
    logging.error(traceback.format_exc())
    cur.close()
    conn.close()


