"""ロガーの名前をsimpleExampleにして作成"""
import logging.config

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')