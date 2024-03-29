import logging
import threading
import time


logging.basicConfig(
  level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
  logging.debug('start')
  lock.acquire()
  i = d['X']
  time.sleep(5)
  d['X'] = i + 1
  logging.debug(d)
  lock.release()
  logging.debug('end')
 
def worker2(d, lock):
  logging.debug('start')
  lock.acquire()
  i = d['X']
  d['X'] = i + 1
  logging.debug(d)
  lock.release()
  logging.debug('end')
  
if __name__ == '__main__':
    d = {'X': 0}
    t1 =  threading.Thread(target=worker1, args=(d, ))
    t2 =  threading.Thread(target=worker2, args=(d, ))
    t1.start()
    t2.start()
    