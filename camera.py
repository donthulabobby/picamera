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
videoRecordingsDir = "/opt/piCamRecordings/"
historyNumDaysForRecordings = 7
location = "/var/pi/picam.db"
table_name = "pi_videos"
conn = lite.connect(location)
cur = conn.cursor()


def insertIntoTable( dateTimeNow, filePath, cursor, connection ):
  logging.info("inserting, " + filePath + " into table " + table_name)
  sql = "insert into " + table_name + "(timestamp, file) values (DATETIME('" + str(dateTimeNow) + "'), '" + filePath + "')"
  cursor.execute(sql)
  connection.commit()

def deleteVideoFile( filePath ):
  logging.info("deleting file, " + str(filePath))
  os.remove(str(filePath))

def deleteOldVideos( timestamp, cursor, connection ):
  deleteTime = timestamp - datetime.timedelta(days=historyNumDaysForRecordings)
  cursor.execute("SELECT file FROM " + table_name + "  WHERE timestamp < DATETIME('" + str(deleteTime) + "')")
  rows = cur.fetchall()
  for row in rows:
    deleteVideoFile(row[0])
  cursor.execute("DELETE FROM " + table_name + "  WHERE timestamp < DATETIME('" + str(deleteTime) + "')")
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
    insertIntoTable(dateTimeNow, videoFilePath, cur, conn)
    logging.info(videoFilePath + ". Recording Time in Seconds: " + str(timeInSecsToRecord))
    camera.start_recording(videoFilePath)
    camera.wait_recording(timeInSecsToRecord)
    camera.stop_recording()
    deleteOldVideos(dateTimeNow,cur,conn)
  except Exception as e:
    logging.error("Error happened while recording: " + videoFilePath)
    logging.error(traceback.format_exc())
    cur.close()
    conn.close()


