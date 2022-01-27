import json
from datetime import datetime


def logger(object, showTime=True):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if showTime:
        print('[%s]:' % time, object)
    else:
        print(object)


def json_load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as err:
        logger('Error json load: {}'.format(err))
    return None


def json_update(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            return json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as err:
        logger('Error json update: {}'.format(err))
    return None
