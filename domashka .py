import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(message)s',)

logging.info("xxx")
