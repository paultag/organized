# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.db import db

class Importer:
    def __init(self, project):
        self._project = project


    def save_bug(self, bug):
        bug = bug.update({
            "_project": self._project
        })
        ret = db.issues.update({"_id": bug['_id']},
                         bug,
                         True,
                         safe=True)
        return ret['n'] == 1
