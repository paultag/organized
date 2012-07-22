# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log
import json

API_BASE = "https://api.github.com"
PREFIX = "github"

def unmangle(obj, package):
    issue_migration = {
        "assignee": "owner",
        "labels": "tags",
        "user": "reporter"
    }
    for mig in issue_migration:
        obj[issue_migration[mig]] = obj[mig]
        del(obj[mig])
    obj['_id'] = create_id(
        PREFIX,
        "bug",
        package,
        obj['number']
    )
    return obj


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
        payload = self._get_json(url)
        count = 0
        for bug in payload:
            bug = unmangle(bug, "%s_%s" % (
                self._owner,
                self._project
            ))
            self.save_bug(bug)
            count += 1
        return count


    def _get_all_issues(self, **kwargs):
        log("Getting issues.")
        counter = 1
        numup = -1
        while numup != 0:
            numup = self._get_issue_page(counter, **kwargs)
            counter += 1


    def update(self):
        log("Getting open issues.")
        self._get_all_issues(state='open')
        log("Getting closed issues.")
        self._get_all_issues(state='closed')
