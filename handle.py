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

    def find_child_by_id(self, parent, id_child):
        return parent.sibling(packageName=PACKGE_NAME, resourceId='{}:id/{}'.format(PACKGE_NAME, id_child))

    def find_child_by_class(self, parent, class_name):
        return parent.sibling(
            packageName=PACKGE_NAME, className=class_name)

    def find_child_by_desc(self, parent, desc):
        return parent.sibling(
            packageName=PACKGE_NAME, description=desc)
