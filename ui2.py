from time import sleep

import uiautomator2 as u2
import util
from consts import *

d = u2.connect()
sessApp = d.session(CLASS_NAME_APP, attach=True)
sessApp.make_toast('Auto Bot start attach Intagram', 2)


def switchPostInSaved(index):
    while(getDataFromId("image_button") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    util.logger('Switch post in saved %d' % index)
    getDataFromId("image_button")[index].click()


def switchSaved():
    util.logger('Switch saved')
    dataList = getDataFromId('recycler_view')
    if dataList.child(className=CLASS_NAME_BUTTON):
        return dataList.child(className=CLASS_NAME_BUTTON)[INDEX_MENU_OPTION_SAVED].click()
    return dataList.child(className=CLASS_NAME_LINEAR_LAYOUT)[INDEX_MENU_OPTION_SAVED].click()


def switchUser(index):
    while(getDataFromId("row_user_textview") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    users = getDataFromId("row_user_textview")
    util.logger('Switch user %d' % index)
    return users[index].click()


def getLinkVideo(username):
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

    code = util.getCodeFromLink(sessApp.clipboard)
    resultDonwload = util.downloadVideoIG(username, code)
    if resultDonwload == None:
        util.logger('Download video failed')
    else:
        util.logger('Download video successfull: %s' % resultDonwload)
        fileName = '/{}/{}/{}.mp4'.format(
            util.PATH_SAVE_FILE_MEDIA_ON_PHONE, username, code)
        util.logger('Push mp4 files to phone internal storage ...')
        result = sessApp.push(resultDonwload, fileName, 420, True)
        if result == None:
            util.logger('Error push file mp4 to phone!')
        else:
            util.logger(result)


def showTab(tab):
    if (tab == 'user'):
        util.logger('Show tab switch user')
        return getDataFromId(ID_TAB_PROFILE).long_click()
    elif (tab == 'option'):
        util.logger('Show tab switch option')
        return sessApp(description=DESC_BUTTON_OPTION,
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
    while(getDataFromId(ID_TEXT_USERNAME, "text") == None):
        util.logger('Waitting ...')
        sleep(2.5)
    util.logger('Get info user')
    username = getDataFromId(ID_TEXT_USERNAME, "text")
    fullname = getDataFromId(ID_TEXT_FULLNAME, "text")
    posts = getDataFromId(ID_TEXT_COUNT_POSTS, "text")
    followers = getDataFromId(ID_TEXT_COUNT_FOLLOWERS, "text")
    following = getDataFromId(ID_TEXT_COUNT_FOLLOWING, "text")
    return {
        'username': username,
        'fullname': fullname,
        'posts': posts,
        'followers': followers,
        'following': following
    }


def getDataListFromIdDevice(device=None):
    if not device:
        return sessApp(className=CLASS_NAME_LIST_VIEW, resourceId=CLASS_NAME_ANDROID + ":id/list")
    else:
        return device.child(className=CLASS_NAME_LIST_VIEW, resourceId=CLASS_NAME_ANDROID + ":id/list")


def getDataFromId(id, type="full", text=''):
    resultInfo = None
    if(text == ''):
        resultInfo = sessApp(resourceId=CLASS_NAME_APP + ":id/" + id)
    else:
        resultInfo = sessApp(resourceId=CLASS_NAME_APP +
                             ":id/" + id, text=text)
    if(resultInfo.exists):
        if type == "full":
            return resultInfo
        else:
            return resultInfo.info[type]
    else:
        return None
