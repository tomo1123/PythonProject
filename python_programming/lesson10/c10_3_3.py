'''ログをメールで送信する'''
import logging
import logging.handlers


smtp_host = 'smtp-mail.outlook.com'
smtp_port = 587

from_email = 'test@example.com'
to_email = 'test@example.com'
username = 'test@example.com'
password = 'feiwafjdafjeiwaf'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')