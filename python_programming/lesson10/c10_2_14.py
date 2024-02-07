"""logtest.pyのdo_somethingを実行"""
import logging

import logtest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('from main')
logtest.do_something()