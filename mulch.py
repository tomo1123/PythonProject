import logging
import threading
import time


logging.basicConfig(
  level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d):
  logging.debug('start')
  i = d['X']
  logging.debug('end')
 
def worker2():
  logging.debug('start')
  logging.debug('end')
  
if __name__ == '__main__':

    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.daemon = True
        t.start()
    for thread in threading.enumerate():
        if thread is threading.current_thread():
          print(thread)
          continue
        thread.join()