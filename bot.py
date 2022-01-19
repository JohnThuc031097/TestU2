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
            if id_profile.exists(timeout=2):
                id_profile.click()
        elif id_screen == ID_SCREEN_SELECT_USERS:
            id_profile = self.bot.find_by_id('profile_tab')
            if id_profile.exists(timeout=2):
                id_profile.long_click()
        elif id_screen == ID_SCREEN_OPTIONS:
            id_options = self.bot.find_by_desc('Options')
            if id_options.exists(timeout=2):
                id_options.click()
        elif id_screen == ID_SCREEN_VIDEOS_SAVED:
            id_saved = self.bot.find_by_desc('Saved')
            if id_saved.exists(timeout=2):
                id_saved.click()
                id_saved_thumbnail = self.bot.find_by_id(
                    'saved_collection_thumbnail')
                if id_saved_thumbnail.exists(timeout=2):
                    id_saved_thumbnail.click(timeout=5)
                    id_items_video_saved = self.bot.find_by_id(
                        'profile_tab_icon_view')
                    if id_items_video_saved.exists(timeout=2):
                        id_items_video_saved.click(timeout=5)

    def set_user(self, user):
        if not self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
            self.switch_screen(ID_SCREEN_SELECT_USERS)
        if user.exists(timeout=2):
            user.click(timeout=2)
            if self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
                self.bot.sess.press('back')

    def get_items_videos_saved(self):
        id_items_videos_saved = self.bot.find_by_id(
            'clips_tab_grid_recyclerview')
        if id_items_videos_saved.exists(timeout=2):
            return self.bot.find_child_by_class(id_items_videos_saved, 'android.widget.RelativeLayout')

    def get_all_users(self):
        data_users = {}
        if not self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
            self.switch_screen(ID_SCREEN_SELECT_USERS)
        users = self.bot.find_by_id('row_user_textview')
        if users.exists(timeout=2):
            if users.count > 2:
                for i in range(users.count-1):
                    data_users[users[i].info['text']] = users[i]
        return data_users