"""mapで実行"""
import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])

def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r

if __name__ == '__main__':
    main()