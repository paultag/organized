# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log

import json

API_BASE = "https://api.github.com"

class GitHub(Importer):
    def __init__(self, owner, project):
        log("Created github instance. %s/%s" % (
            owner, project
        ))
        self._owner = owner
        self._project = project


    def _get_json(self, url):
        payload = json.loads(self.load_url(url))
        return payload


    def _get_issue_page(self, page, **kwargs):
        log("Getting page %s" % (page))

        kwargs.update({"page": page})

        keyword_args = self.safe_urlencode(
            kwargs
        )
        url = "%s/repos/%s/%s/issues?%s" % (
            API_BASE,
            self._owner,
            self._project,
            keyword_args
        )
        print url


    def _get_all_issues(self):
        log("Getting issues.")
        counter = 1
        numup = -1
        while numup != 0:
            numup = self._get_issue_page(counter)
            counter += 1


    def update(self):
        self._get_all_issues()
