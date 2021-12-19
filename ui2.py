from time import sleep
import uiautomator2 as u2
import util

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
    return getDataListFromIdDevice().child(
        className=CLASS_NAME_BUTTON)[INDEX_MENU_OPTION_SAVED].click()


def switchUser(index):
    while(getDataFromId("row_user_textview") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    users = getDataFromId("row_user_textview")
    util.logger('Switch user %d' % index)
    return users[index].click()


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


def getDataFromId(id, type="full"):
    resultInfo = dUi2(resourceId=CLASS_NAME_APP + ":id/" + id)
    if(resultInfo.exists):
        if type == "full":
            return resultInfo
        else:
            return resultInfo.info[type]
    else:
        return None
