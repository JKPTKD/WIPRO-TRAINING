import logging
 
logging.basicConfig(
    filename='testPrg.log',
    level=logging.DEBUG,
    format='%(asctime)s -> %(levelname)s -> %(message)s'
    )
 
logging.debug('This is an debug level message')
logging.info('This is an Info level message')
logging.warning('This is an warning level message')