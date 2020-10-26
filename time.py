from random import randint
import time
from datetime import datetime,timedelta
from threading import Timer


score  = 0

while True:
    t = f'{randint(0,10):02d}:{randint(0,59):02d}'
    curr = datetime.strptime(t,'%M:%S')
    new = curr + timedelta(seconds=30)

    tcurr = f'{curr.time().minute:02d}:{curr.time().second:02d}'
    tnew = f'{new.time().minute:02d}:{new.time().second:02d}'

    

    timeout = 4
    t = Timer(timeout, print, [ tnew ])
    t.start()
    prompt = "%s ===> " % tcurr
    answer = input(prompt)

    if answer == f'{new.time().second:02d}':
        print("nice!")
    else:
        print("failed")
    


    t.cancel()


    



