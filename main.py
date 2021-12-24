import ui2
import util


userInfo = ui2.getInfoUser()
util.logger(userInfo, False)

ui2.showTab('option')
ui2.switchSaved()

ui2.showTab('all_post_saved')
ui2.switchPostInSaved(2)

ui2.getLinkVideo(userInfo['username'])
