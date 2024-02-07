"""formatを使ったログの書き方"""
import logging

logging.basicConfig(level=logging.INFO)

logging.info('info {}'.format('test'))