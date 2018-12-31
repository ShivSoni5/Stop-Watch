import time

print('Press Enter to start and Ctrl+C to stop')

while True:
    try:
        input()
        starttime=time.time()
        print('Started')
        while True:
            seconds=round(time.time()-starttime,0)
            print('Time Elapsed: ',seconds,'seconds',end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:',round(endtime-starttime,2),'seconds')
        break
