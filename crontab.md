# Crontab entries

@reboot cd /home/pi/code/gardenpi && sudo python webserver.py 80 &

@reboot cd /home/pi/code/gardenpi && sudo python3 thermalmonitor.py &

@reboot cd /home/pi/code/gardenpi && sudo python3 chargecontroller.py &

*/30 * * * * cd /home/pi/code/gardenpi && sudo python3 pumpcontroller.py &

*/15 * * * * cd /home/pi/code/gardenpi && sudo python3 ipmailer.py &

@reboot cd /home/pi/code/gardenpi && sudo python3 phonecharger.py &
