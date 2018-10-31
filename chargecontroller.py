#
#
#

import os
import time
import gpiozero
import db

from consts import CHARGER_GPIO
from consts import CHARGER_RUNTIME
from consts import CHARGER_OFFTIME

chargeRelay = gpiozero.OutputDevice(CHARGER_GPIO, active_high = False,
                                  initial_value = False)
                                  
chargeState = False
while True:
    # Start charging
    chargeRelay.on()
    entry = { 'timestamp': str(datetime.now().timestamp()),
                'event': 'Switch On'}
    db.logChargeRun(entry)

    time.sleep(CHARGER_RUNTIME)

    # Stop charging charging
    chargerRelay.off()
    entry = { 'timestamp': str(datetime.now().timestamp()),
                'event': 'Switch Off'}
    db.logChargeRun(entry)

    time.sleep(CHARGER_OFFTIME)