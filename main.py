from random import random
from bot import BotInstagram
from consts import *
import util

json_setting = util.load_json('settings.json')
if json_setting != None:
    bot = BotInstagram()
    bot.switch_screen(ID_SCREEN_PROFILE)
    users = bot.get_users()
    if len(json_setting['users']) > 0:
        for name in json_setting['users']:
            user_crr = users[name]
            bot.set_user(user_crr)
            bot.switch_screen(ID_SCREEN_OPTIONS)
            bot.switch_screen(ID_SCREEN_VIDEOS_SAVED)
            items = bot.get_items_videos_saved()
            index_random = random.randint(0, items-1)
            bot.select_item_video_saved(items[index_random])
            break
