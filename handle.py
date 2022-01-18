import uiautomator2 as u2

from consts import *


class HandleU2:
    def __init__(self):
        self.sess = u2.connect().session(PACKGE_NAME, attach=True)
        self.sess.make_toast('Auto Bot start attach Instagram', 2)

    def find_by_id(self, id):
        return self.sess(
            packageName=PACKGE_NAME, resourceId='{}:id/{}'.format(PACKGE_NAME, id))

    def find_by_desc(self, desc):
        return self.sess(
            packageName=PACKGE_NAME, description=desc)
