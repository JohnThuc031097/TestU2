import random
from bot import BotInstagram
from consts import *
import util

setting = util.json_load('settings.json')
if setting != None:
    bot = BotInstagram()
    bot.switch_screen(ID_SCREEN_PROFILE)
    users = bot.get_users()
    if len(setting['users']['bot']) > 0:
        for name in setting['users']['bot']:
            if bot.set_user(users[name]):
                if bot.switch_screen(ID_SCREEN_OPTIONS):
                    if bot.switch_screen(ID_SCREEN_VIDEOS_SAVED):
                        index_video = 0
                        items = bot.get_items_video_saved()
                        if items.count > 1:
                            index_video = random.randint(0, items.count-1)
                            bot.download_video_by_login(
                                items[index_video], None)
            break
