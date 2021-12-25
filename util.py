import instaloader

import glob
import os
import json
import pathlib
from datetime import datetime

FILE_NAME_SETTING = 'settings.json'
FOLDER_NAME_SESSIONS = 'sessions'
FOLDER_NAME_VIDEOS = 'videos'
WEB_HOST = 'https://www.instagram.com'
PATH_SAVE_FILE_MEDIA_ON_PHONE = 'sdcard/AutoBot'


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
        result = None
        if not os.path.isdir('{}\{}\{}'.format(FOLDER_NAME_VIDEOS, username, code)):
            # Load account from file settings JSON
            account = loadJson()['account']
            if account != None:
                # Get path file session
                fileSession = '{}\{}'.format(FOLDER_NAME_SESSIONS, username)
                L = instaloader.Instaloader()
                # Check exist file session
                if not os.path.isfile(fileSession):
                    logger(
                        'Not found file session. Tool will create new file sessions')
                    L.login(username, account[username])
                    L.save_session_to_file(fileSession)
                L.load_session_from_file(username, fileSession)
                if L.test_login() == None:
                    L.login(username, account[username])
                    L.save_session_to_file(fileSession)
                    L.load_session_from_file(username, fileSession)
                    if L.test_login() == None:
                        return result

                profile = instaloader.Profile.from_username(
                    L.context, username)
                for saved_post in profile.get_saved_posts():
                    if code == saved_post.shortcode:
                        if L.download_post(saved_post, pathlib.Path('{}\{}\{}'.format(FOLDER_NAME_VIDEOS, username, saved_post.shortcode))):
                            nameVideoSaved = str(saved_post.date_utc).replace(
                                ' ', '_').replace(':', '-')
                            result = '{}\{}\{}\{}_UTC.mp4'.format(
                                FOLDER_NAME_VIDEOS, username,  saved_post.shortcode, nameVideoSaved)
                        break
        else:
            logger('Video file already exists => skipping ...')
            result = glob.glob(
                '{}\{}\{}\*.mp4'.format(FOLDER_NAME_VIDEOS, username, code))[0]
    except Exception as err:
        logger('Error download video: {}'.format(err))
    return result


def loadJson():
    try:
        with open(FILE_NAME_SETTING) as f:
            return json.load(f)
    except Exception as err:
        logger('Error load json: {}'.format(err))
    return None
