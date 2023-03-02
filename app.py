import os
import logging
import argparse
import random
import sys
import time
import schedule

from time import sleep

# ETL
import extract
import transform
import load
from extract_json import data


url = os.environ.get("BLOOMBERG_URL_2")
scripts_server = os.environ.get("SCRIPTS_SERVER")


def get_options(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--live', default=False, type=bool, help='Run live or localhost')
    parser.add_argument('-u', '--url', default= url, help = 'URL key name or File to Parse. 1-year is the default')

    parser.add_argument('-a', '--use_server', default=False, type=bool, help = 'Save to server or no')
    parser.add_argument('-s', '--server', default=scripts_server, help = 'server key name or File to Parse. All is the default')


    parser.add_argument('-p', '--proxy', default=False, type=bool, help='Run with proxies or without')
    parser.add_argument('-v', '--verbose', default=False, type=bool, help='Allow more logging messages')

    return parser.parse_args()

args = get_options(sys.argv)

# logging
if args.verbose:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
else:
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.info(args)
logger.info("Starting logger")




def etl_page(symbol):
    try:
        if args.live == True:
            d = extract.daily(symbol, args.proxy, args.url, logger)
            logger.info('Going live')
        else:
            d = data
            logger.info('Using local file ONLY')
        final_object = transform.Parse(d)
        load.Preview(final_object)
        load.send_to_server_ds(args.use_server, args.server, final_object)
    except Exception as e:
        logger.error(str(e))

def main(symbols, url, server, use_proxy, use_server):
    for sym in symbols:
        logger.info('Symbol' + sym)
        etl_page(sym)

'''
def run_on_schedule(func, urls, interval, start, end):
    while True:
        try:
            now = datetime.datetime.now()
            hour = now.hour
            weekday = now.weekday()
            if hour >= start and hour <= end and weekday < 5:
                logging.info("The script will run now")
                func(urls)
                time_to_sleep = interval * 60
                logging.info("Will sleep for {} minutes".format(interval))
                sleep(time_to_sleep)
            elif (weekday >= 5) or (weekday == 4 and hour > end):
                next_w_day_start = (now + datetime.timedelta(days=(7-weekday))).replace(hour=start, minute=0, second=0)
                time_to_sleep = (next_w_day_start-now).total_seconds()
                logging.info("Will sleep for {} minutes until Monday {} o'clock".format(round(time_to_sleep/60), start))
                sleep(time_to_sleep)
            elif hour < start:
                w_day_start = now.replace(hour=start, minute=0, second=0)
                time_to_sleep = (w_day_start-now).total_seconds()
                logging.info("Will sleep for {} minutes until {} o'clock".format(round(time_to_sleep/60), start))
                sleep(time_to_sleep)
            else:
                next_w_day_start = (now + datetime.timedelta(days=1)).replace(hour=start, minute=0, second=0)
                time_to_sleep = (next_w_day_start-now).total_seconds()
                logging.info("Will sleep for {} minutes until tomorrow {} o'clock".format(round(time_to_sleep/60), start))
                sleep(time_to_sleep)
        except Exception as e:
            logging.error(str(e))

logging.info("The script will run every {} minutes between {} and {} Mon-Fri".format(args.interval, args.start, args.end))
'''

symbols = ['BSX:IND', 'CRYTR:IND', 'CRSMBCT:IND', 'MSETOP:IND']

if __name__ == '__main__':

    main(symbols, url, args.proxy, args.use_server, args.server)

    # run_on_schedule(main, URLs, args.interval, args.start, args.end)





# end
