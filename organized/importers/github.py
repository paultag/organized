# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log

import json

class GitHub(Importer):
    def __init__(self, owner, project):
        log("Created github instance. %s/%s" % (
            owner, project
        ))
        self._owner = owner
        self._project = project

    def _load_url(self, url):
        pass


    def _get_json(self, url):
        payload = json.loads(self.load_url(url))
        return payload


    def _get_issue_page(self, page):
        log("Getting page %s" % (page))
        pass


    def _get_all_issues(self):
        log("Getting issues.")
        counter = 1
        numup = -1
        while numup != 0:
            numup = self._get_issue_page(counter)
            counter += 1


    def update(self):
        self._get_all_issues()
