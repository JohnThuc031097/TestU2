import random
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
            if users[name]:
                bot.set_user(users[name])
                bot.switch_screen(ID_SCREEN_OPTIONS)
                bot.switch_screen(ID_SCREEN_VIDEOS_SAVED)
                index_video = 0
                items = bot.get_items_videos_saved()
                if items.count > 1:
                    index_video = random.randint(0, items.count-1)
                bot.select_item_video_saved(items[index_video])
                bot.download_video()
                bot.remove_video_saved(items[index_video])
