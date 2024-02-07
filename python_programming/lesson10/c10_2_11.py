"""ロガーの名前を変更する"""
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
logger.debug('debug')