import uiautomator2 as u2
import util

from consts import *

dUi2 = u2.connect()


def switchSaved():
    util.logger('Switch saved')
    d = getDataFromId(ID_TAB_PROFILE_MENU)
    util.logger(getDataFromIdDevice(d).child(
        className=CLASS_NAME_BUTTON))


def switchUser(index):
    users = getDataFromId("row_user_textview")
    util.logger('Switch user %d' % index)
    return users[index].click()


def showTabSwitchOption():
    util.logger('Show tab switch option')
    getDataFromDescByBtn(DESC_BUTTON_OPTION).click()


def showTabSwitchUser():
    util.logger('Show tab switch user')
    return getDataFromId(ID_TAB_PROFILE).long_click()


def getInfoUser():
    util.logger('Get info user')
    getDataFromId(ID_TAB_PROFILE).click()
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


def getDataFromId(id):
    return dUi2(resourceId=CLASS_NAME_APP + ":id/" + id)


def getDataFromIdDevice(device):
    return device.child(resourceId=CLASS_NAME_ANDROID + ":id/list")


def getDataFromDescByText(desc):
    return dUi2(description=desc, className=CLASS_NAME_TEXT)


def getDataFromDescByBtn(desc):
    return dUi2(description=desc, className=CLASS_NAME_BUTTON)


def getDataFromId(id, type="full"):
    resultInfo = getDataFromId(id)
    if(resultInfo.exists):
        if type == "full":
            return resultInfo
        else:
            return resultInfo.info[type]
    else:
        return "none"
