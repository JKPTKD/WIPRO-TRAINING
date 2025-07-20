# DAY10 Q2
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: logging
'''
import logging

logging.basicConfig(
    filename='testPrg.log',
    level=logging.DEBUG,
    format='%(asctime)s -> %(levelname)s -> %(message)s'
)

logging.debug('This is an debug level message')
logging.info('This is an Info level message')
logging.warning('This is an warning level message')