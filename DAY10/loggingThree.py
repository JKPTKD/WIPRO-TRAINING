import logging
 
logging.basicConfig(
    filename='testPrg.log',
    level=logging.DEBUG,
    format='%(asctime)s -> %(levelname)s -> %(message)s'
    )
 
 
try:
    10 / 0.0
except ZeroDivisionError as e:
    logging.exception('Exception Occurred!')