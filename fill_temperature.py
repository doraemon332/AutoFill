import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/xxxxxxxx/formResponse'

# Get payload from your google doc response header
payload = {
    'entry.1035399214' : 'name name ',
    'entry.1300365472' : '36.3',
    'entry.245438671'  : '',
    'draftResponse' : '[]',
    'pageHistory' : '0',
    'fbzx' : '-xxxxxx'
}


num = 1  # number of executions
period = np.arange(0.5, 5.0, 0.1)
delay = 0  # delay of execution
while num > 0:
    try:
        # ranodmize temperature
        payload['entry.1300365472'] = random.randrange(360, 366) / 10.0
        res = rq.post(url, data=payload)
        res.raise_for_status()
        if res.status_code == 200 :
            delay = round(random.choice(period), 2)  # round off to the 2nd decimal place
            print('Fill Out : ' + payload['entry.1035399214'] + ' delay : ' + str(delay) + ' sec')
            time.sleep(delay)
    except rq.HTTPError:
        print('HTTP Error!')
    
    num -= 1
