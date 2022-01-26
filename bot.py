import util
import handle
from consts import *


class BotInstagram:
    def __init__(self):
        util.logger('Start Bot Instagram v1.0 by ThucNobita')
        self.bot = handle.HandleU2()

    def switch_screen(self, id_screen):
        util.logger('Switch screen: {}'.format(id_screen))
        if id_screen == ID_SCREEN_PROFILE:
            return self.bot.find_by_id('profile_tab').click_exists(timeout=2):
        elif id_screen == ID_SCREEN_SELECT_USERS:
            id_profile = self.bot.find_by_id('profile_tab')
            if id_profile.exists(timeout=2):
                return id_profile.long_click()
            return False
        elif id_screen == ID_SCREEN_OPTIONS:
            return self.bot.find_by_desc('Options').click_exists(timeout=2)
        elif id_screen == ID_SCREEN_UPLOAD_REEL:
            if self.switch_screen(ID_SCREEN_PROFILE):
                if self.bot.find_by_desc('Create New').click_exists(timeout=2):
                    if self.bot.find_by_desc('Reel').click_exists(timeout=2):
                        self.bot.find_by_id(
                            'auxiliary_button').click_exists(timeout=2)
                        if self.bot.find_by_id('dial_ar_effect_picker_left_side_button_container').click_exists(timeout=2):
                            if self.bot.find_by_id('gallery_folder_menu').click_exists(timeout=2):
                                if self.bot.find_by_desc('Instagram').click_exists(timeout=2):
                                    return True

            return False
        elif id_screen == ID_SCREEN_VIDEOS_SAVED:
            if self.bot.find_by_desc('Saved').click_exists(timeout=2):
                if self.bot.find_by_id('saved_collection_thumbnail').click_exists(timeout=5):
                    return self.bot.find_by_desc('Saved reels').click_exists(timeout=5)
            return False

    def remove_video_saved(self, item_selected):
        util.logger('Remove video: Select item')
        if self.bot.find_by_desc('Options').click_exists(timeout=2):
            if self.bot.find_by_text('Select…').click_exists(timeout=2):
                if item_selected.click_exists(timeout=2):
                    if self.bot.find_by_id('remove_button').click_exists(timeout=2):
                        self.bot.find_by_text('Unsave').click_exists(timeout=2)
                        util.logger('Remove video: Removed')
                        return True
        return False

    def set_user(self, user):
        util.logger('Set user: {}'.format(user.info['text']))
        if self.switch_screen(ID_SCREEN_SELECT_USERS):
            if user.click_exists(timeout=2):
                if self.bot.find_by_id('bottom_sheet_container_view').exists(timeout=2):
                    self.bot.sess.press('back')
                    return True
        return False

    def select_item_video_saved(self, item_selected):
        util.logger('Select video: click')
        return item_selected.click_exists(timeout=2)

    def get_items_videos_saved(self):
        result = []
        id_items_videos_saved = self.bot.find_by_id(
            'clips_tab_grid_recyclerview')
        if id_items_videos_saved.exists(timeout=2):
            items = self.bot.find_child_by_class(
                id_items_videos_saved, 'android.widget.RelativeLayout')
            if items.exists(timeout=2):
                result = items
        return result

    def get_users(self):
        util.logger('Get users')
        data_users = {}
        if self.switch_screen(ID_SCREEN_SELECT_USERS):
            users = self.bot.find_by_id('row_user_textview')
            if users.exists(timeout=2):
                if users.count > 2:
                    for i in range(users.count-1):
                        data_users[users[i].info['text']] = users[i]
        return data_users

    def download_video(self):
        util.logger('Download video: Select video')
        if self.bot.find_by_id('direct_share_button').click_exists(timeout=4):
            if self.bot.find_by_desc('Add reel to your story').click_exists(timeout=10):
                if self.bot.find_by_id('overflow_button').click_exists(timeout=2):
                    if self.bot.find_by_id('gallery_menu_save').click_exists(timeout=2):
                        util.logger('Download video: Start')
                        # waiting download
                        msg_processing = self.bot.find_by_id('message')
                        if msg_processing.exists(timeout=2):
                            msg_processing.wait_gone(timeout=(60*10))
                            util.logger('Download video: Saved')
                            self.bot.sess.press('back')
                            self.bot.find_by_desc(
                                'Discard video').click_exists(timeout=4)
                            self.bot.sess.press('back')
                            self.bot.find_by_desc(
                                'Back').click_exists(timeout=2)
                            util.logger('Download video: End')
                            return True
        return False
