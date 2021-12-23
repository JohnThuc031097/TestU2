from logging import log
import instaloader

import glob
import os
import json
from datetime import datetime

FILE_SETTING = 'setting.json'
WEB_HOST = 'https://www.instagram.com'
PATH_SAVE_FILE_MEDIA_ON_PHONE = '/sdcard/AutoBot/'


def logger(object, showTime=True):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if showTime:
        print('[%s]:' % time, object)
    else:
        print(object)


def getCodeFromLink(link):
    if str(link).find(WEB_HOST, 0) != -1:
        codeTmp = str(link).replace(
            '/?utm_medium=copy_link', '').split('/')
        code = codeTmp[len(codeTmp)-1]
        logger('Get code video: %s' % code)
        return code
    return None


def downloadVideoIG(username, code):
    try:
        result = []
        if not os.path.isdir(code):
            account = loadJson()['account']
            if account != None:
                L = instaloader.Instaloader()
                # L.login(username, account[username])
                L.load_session_from_file()
                profile = instaloader.Profile.from_username(
                    L.context, username)
                for saved_post in profile.get_saved_posts():
                    if code == saved_post.shortcode:
                        result = L.download_post(
                            saved_post, saved_post.shortcode)
                        if not result:
                            return logger('Error download video')
                        pathFile = str(saved_post.date_utc).replace(
                            ' ', '_').replace(':', '-') + '_UTC.mp4'
                        result = [code, pathFile]
        else:
            logger('Video file already exists => skipping ...')
            result = [code, str(glob.glob(code + "/*.mp4")[0]).split('\\')[1]]
    except Exception as err:
        logger('Error download video: {}'.format(err))
    return result


def loadJson():
    try:
        with open(FILE_SETTING) as f:
            return json.load(f)
    except Exception as err:
        logger('Error load json: {}'.format(err))
    return None
