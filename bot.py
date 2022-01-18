from socket import timeout
import util
import handle
from consts import *


class BotInstagram:
    def __init__(self):
        util.logger('Start Bot Instagram v1.0')
        self.bot = handle.HandleU2()

    def switch_screen(self, id_screen):
        util.logger('Switch screen: {}'.format(id_screen))
        if id_screen == ID_SCREEN_PROFILE:
            id_profile = self.bot.find_by_id('profile_tab')
            if id_profile != None:
                id_profile.click()
        elif id_screen == ID_SCREEN_SELECT_USERS:
            id_profile = self.bot.find_by_id('profile_tab')
            if id_profile != None:
                self.bot.sess.implicitly_wait(2)
                id_profile.long_click()
        elif id_screen == ID_SCREEN_OPTIONS:
            id_options = self.bot.find_by_desc('Options')
            util.logger(id_options)
            if id_options != None:
                self.bot.sess.implicitly_wait(2)
                id_options.click()

    def set_user(self, user):
        if not self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
            self.switch_screen(ID_SCREEN_SELECT_USERS)
        if user.exists(timeout=2):
            user.click()

    def get_all_users(self):
        data_users = {}
        if not self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
            self.switch_screen(ID_SCREEN_SELECT_USERS)
        users = self.bot.find_by_id('row_user_textview')
        if users.count > 2:
            for i in range(users.count-1):
                data_users[users[i].info['text']] = users[i]
        return data_users
