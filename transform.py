from extract_json import data
from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)



def Parse(d):
    logger.info('Transforming Data.')
    try:
        all_day = d[0]["price"]
        logger.info('{} datapoints!'.format(len(all_day)))
        historical = {}
        for point in all_day:
            object_to_send = {}
            object_to_send["c"] = float(point["value"])
            historical[point["date"]] = object_to_send

        final_object = {
            "symbol": 'BSX:IND',
            "historical": historical,
            "source": "bloom:price:BloomUpd"
        }

        # logger.info(final_object)
        return final_object

    except Exception as e:
        logger.error(str(e))




# Parse(data)



# end
