import json
from bot import BotInstagram
from consts import *
import util

json_setting = util.load_json('settings.json')
if json_setting != None:
    bot = BotInstagram()
    users = bot.get_all_users()
    if len(json_setting['users']) > 0:
        for user in json_setting['users']:
            user_crr = users[user]
            util.logger(user_crr.info)
            bot.set_user(user_crr)
            bot.switch_screen(ID_SCREEN_OPTIONS)
            break
