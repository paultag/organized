# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.db import db
from organized.util import log

import urllib
import urllib2

class Importer:
    def _init(self, project):
        self._project = project


    def save_bug(self, bug):
        bug.update({
            "_project": self._project
        })
        log("Saving bug %s" % (
            bug['_id']
        ))
        ret = db.bugs.update({"_id": bug['_id']},
                         bug,
                         True,
                         safe=True)
        return ret['n'] == 1


    def load_url(self, url):
        f = urllib2.urlopen(url)
        return f.read()


    def safe_urlencode(self, dic):
        return urllib.urlencode(dic)
