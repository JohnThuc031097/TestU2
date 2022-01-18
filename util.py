import json
from datetime import datetime


def logger(object, showTime=True):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if showTime:
        print('[%s]:' % time, object)
    else:
        print(object)


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as err:
        logger('Error load json: {}'.format(err))
    return None
