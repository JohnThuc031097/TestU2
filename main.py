import ui2
import util

userInfo = ui2.getInfoUser()
util.logger(userInfo, False)

"""
util.logger(ui2.getInfoUser(), False)

ui2.showTab('user')

ui2.switchUser(1)
"""
ui2.showTab('option')
ui2.switchSaved()

ui2.showTab('all_post_saved')
ui2.switchPostInSaved(0)

ui2.getLinkVideo(userInfo['username'])
