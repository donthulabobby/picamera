# PiCamera #
<br />
Personal security Pi-Camera.<br />
Records video 24x7.<br />
Saves an hourly video in the following location, /opt/piCamRecordings/[month]/[day]/[hour]h-[minute]m.h264<br />
<br />
<br />

Prerequisites:<br />
  . Install sqlite3 <br />
  . Run, sudo python createDB.py  - this will create the require tables used by the application. <br />
  
<br />
<br />
Usage:<br />
. Run, 'sudo python camera.py &' command to start the security-cam video recording in the background.<br />
  



