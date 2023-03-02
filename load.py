import json
import os
from time import sleep
from datetime import datetime
import requests
import logging
# import pyodbc


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def Preview(data):
    logger.info('Data Preview')
    # logger.info(data)
    # index
    # for k, v in enumerate(data['historical']):
        # logging.info(str(k) + ' ' + str(v))
    # dict items
    # for k, v in data['historical'].items():
        # logging.info(str(k) + ' '+ str(v))
    logger.info('Loaded data')



def send_to_server_ds(use_server, server, data):
    if use_server:
        # logger.info('Sending {} request to server starting test : {}'.format(data, server))
        logger.info('Sending request to save to server starting test : {}'.format(server))

        # r = requests.post(query, json=s)
        # log('Status of the request: {}'.format(r))
    else:
        logger.error('Do not send to my server.')








# end






# end
