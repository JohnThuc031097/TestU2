import uiautomator2 as u2
import util

import re
import requests
from time import sleep

from consts import *

dUi2 = u2.connect()


def switchPostInSaved(index):
    while(getDataFromId("image_button") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    util.logger('Switch post in saved %d' % index)
    getDataFromId("image_button")[index].click()


def switchSaved():
    util.logger('Switch saved')
    return getDataListFromIdDevice().child(className=CLASS_NAME_LINEAR_LAYOUT)[INDEX_MENU_OPTION_SAVED].click()


def switchUser(index):
    while(getDataFromId("row_user_textview") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    users = getDataFromId("row_user_textview")
    util.logger('Switch user %d' % index)
    return users[index].click()


def getLinkVideo():
    while(getDataFromId("feed_more_button_stub") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    getDataFromId('feed_more_button_stub').click()
    while(getDataFromId("action_sheet_row_text_view") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    getDataFromId(
        'action_sheet_row_text_view', 'full', 'Copy Link').click()
    sleep(2.5)

    util.logger(dUi2.clipboard)
    code = str(dUi2.clipboard).replace(
        'https://www.instagram.com/tv/', '').replace('/?utm_medium=copy_link', '')
    linkVideo = 'https://www.instagram.com/p/{0}'.format(code)
    util.logger(linkVideo)
    """"
    r = requests.get(linkVideo)
    match = re.findall(
        'video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count', r.text)
    util.logger(match)
    util.logger(result.replace('\u0026', '&'))
    """


def showTab(tab):
    if (tab == 'user'):
        util.logger('Show tab switch user')
        return getDataFromId(ID_TAB_PROFILE).long_click()
    elif (tab == 'option'):
        util.logger('Show tab switch option')
        return dUi2(description=DESC_BUTTON_OPTION,
                    className=CLASS_NAME_BUTTON).click()
    elif (tab == 'all_post_saved'):
        util.logger('Show tab switch all_post_saved')
        getDataListFromIdDevice().child(className=CLASS_NAME_LINEAR_LAYOUT).child(
            className=CLASS_NAME_BUTTON)[0].click()


def getInfoUser():
    while(getDataFromId(ID_TAB_PROFILE) == None):
        util.logger('Waitting ...')
        sleep(2.5)
    getDataFromId(ID_TAB_PROFILE).click()
    while(getDataFromId(ID_TEXT_NICKNAME, "text") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    util.logger('Get info user')
    nickname = getDataFromId(ID_TEXT_NICKNAME, "text")
    fullname = getDataFromId(ID_TEXT_FULLNAME, "text")
    posts = getDataFromId(ID_TEXT_COUNT_POSTS, "text")
    followers = getDataFromId(ID_TEXT_COUNT_FOLLOWERS, "text")
    following = getDataFromId(ID_TEXT_COUNT_FOLLOWING, "text")
    return {
        'nickname': nickname,
        'fullname': fullname,
        'posts': posts,
        'followers': followers,
        'following': following
    }


def getDataListFromIdDevice(device=None):
    if not device:
        return dUi2(className=CLASS_NAME_LIST_VIEW, resourceId=CLASS_NAME_ANDROID + ":id/list")
    else:
        return device.child(className=CLASS_NAME_LIST_VIEW, resourceId=CLASS_NAME_ANDROID + ":id/list")


def getDataFromId(id, type="full", text=''):
    resultInfo = None
    if(text == ''):
        resultInfo = dUi2(resourceId=CLASS_NAME_APP + ":id/" + id)
    else:
        resultInfo = dUi2(resourceId=CLASS_NAME_APP + ":id/" + id, text=text)
    if(resultInfo.exists):
        if type == "full":
            return resultInfo
        else:
            return resultInfo.info[type]
    else:
        return None
