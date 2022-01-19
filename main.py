import json
from bot import BotInstagram
from consts import *
import util

json_setting = util.load_json('settings.json')
if json_setting != None:
    bot = BotInstagram()
    bot.switch_screen(ID_SCREEN_PROFILE)
    users = bot.get_all_users()
    if len(json_setting['users']) > 0:
        for user in json_setting['users']:
            user_crr = users[user]
            bot.set_user(user_crr)
            bot.switch_screen(ID_SCREEN_OPTIONS)
            bot.switch_screen(ID_SCREEN_VIDEOS_SAVED)
            items = bot.get_items_videos_saved()
            util.logger(items.count)
            break
