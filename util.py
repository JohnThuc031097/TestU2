from logging import log
import instaloader

import json
from datetime import datetime

FILE_SETTING = 'setting.json'


def logger(object, showTime=True):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if showTime:
        print('[%s]:' % time, object)
    else:
        print(object)


def downloadVideoIG(username, code):
    try:
        account = loadJson()['account']
        if account != None:
            L = instaloader.Instaloader()
            L.login(username, account[username])
            profile = instaloader.Profile.from_username(L.context, username)
            for saved_post in profile.get_saved_posts():
                if code == saved_post.shortcode:
                    L.download_post(saved_post, saved_post.shortcode)
                    pathFile = '{}\{}_UTC.mp4'.format(
                        code, str(saved_post.date_utc).replace(' ', '_').replace(':', '-'))
                    return pathFile
    except Exception as err:
        logger('Error download video: {}'.format(err))
    return None


def loadJson():
    try:
        with open(FILE_SETTING) as f:
            return json.load(f)
    except Exception as err:
        logger('Error load json: {}'.format(err))
    return None
