"""
モジュール内のロガー
モジュール内で異なるログレベルの出力
モジュール内で異なるログレベルの設定
ハンドラーでログの出力先をファイルに設定
"""
import logging

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# h = logging.FileHandler('logtest.log')
# logger.addHandler(h)

def do_something():
    # logging.info('from logtest info')
    logger.info('from logtest')
    # logger.debug('from logtest debug')

