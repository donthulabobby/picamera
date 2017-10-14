import sqlite3 as lite
import os

table_name = "pi_videos"
pifolder = "/var/pi/"
location = pifolder + "picam.db"
if not os.path.exists(pifolder):
  os.makedirs(pifolder)

conn = lite.connect(location)
c = conn.cursor()

sql = "create table if not exists " + table_name + " (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, file TEXT)"
c.execute(sql)

#sql = "insert into " + table_name + " (file) values ('/home/pi')"
#c.execute(sql)

conn.commit()
c.close()
conn.close()



