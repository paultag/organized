# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.db import db

import urllib
import urllib2

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


    def load_url(self, url):
        f = urllib2.urlopen(url)
        return f.read()


    def safe_urlencode(self, dic):
        return urllib.urlencode(dic)
