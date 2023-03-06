import os
import json
import requests
import logging
from time import sleep
from datetime import datetime
from random import choice, randint
from USER_AGENTS_2022 import USER_AGENTS_2022, USER_AGENTS
from PROXIES import proxy_array
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def log(text, begin=''):
    print('{}{} - {}'.format(begin, datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S'), text))



cookie = os.environ.get("COOKIE")

def daily(symbol, use_proxy, url, logger):
    global scheduled_hours, USER_AGENTS
    agent = choice(USER_AGENTS_2022)
    try:
        headers = {
            'user-agent': agent,
            'Accept': 'application/json',
            'Accept-Encoding': '*', 
            'Accept-Language': 'en-US,en;q=0.9',
            "Cookie": cookie,
            'Pragma': 'no-cache'
        }

        proxy = choice(proxy_array)
        logger.info("Proxy: " + proxy)
        logger.info('something')
        data = {"hostname": host1,
            "path": path1 + symbol + url,
            "method": "GET",
            "port": 443,
            "headers": headers}
        # logger.info('data', data)
        if (use_proxy):
            r = requests.post(proxy, json=data)
            logger.info('Use proxy')
        else:
            r = requests.get(path + symbol + url, headers=headers)
            logger.info('No proxy for u')

        j = r.json()
        # logger.info('j', j)
        logger.info('got data')

        outFile = open('extract.txt', 'w')
        outFile.write(json.dumps(j))
        outFile.close()
        print('written to the file')

        return j


    except Exception as e:
        # USER_AGENTS.remove(agent)

        logger.error('Did not get valid response: {}. Error: {}.'.format(type(e), e))
        logger.error('Trying again in a few seconds for symbol: {}'.format(symbol))
        sleep(randint(20, 60))
        # retry
        return daily(symbol, use_proxy, url, logger)

'''
symbols = ['BSX:IND', 'CRYTR:IND', 'CRSMBCT:IND', 'MSETOP:IND']




daily(symbols[0], False, url)
'''


