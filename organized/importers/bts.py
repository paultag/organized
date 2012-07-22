# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log
import datetime as dt
import SOAPpy

url = 'http://bugs.debian.org/cgi-bin/soap.cgi'
namespace = 'Debbugs/SOAP'
server = SOAPpy.SOAPProxy(url, namespace)
PREFIX = "bts"

class BTS(Importer):
    def __init__(self, package, root_project):
        log("Created bts instance. %s" % (
            package
        ))
        self._package = package
        self._init(root_project)


    def _import_bugs(self, *args):
        bugs = server.get_bugs(*args)
        # print args, bugs
        objs = server.get_status(bugs)
        objs = objs['item']

        for bug in objs:
            bug = bug['value']
            tags = bug['tags'].split()
            if bug['pending'] != "":
                tags.append("pending")

            tags = [{'name': x} for x in tags]
            bugobj = {
                "_id": create_id(
                    PREFIX,
                    "bug",
                    self._package,
                    bug['bug_num']
                ),
                "tags": tags,
                "body": "XXX: Fixme",
                "title": bug['subject'],
                "opened_at": dt.datetime.fromtimestamp(bug['date']),
                "updated_at": dt.datetime.fromtimestamp(bug['last_modified']),
                "closed_at": "",
                "url": "http://bugs.debian.org/%s" % (bug['bug_num']),
                "owner": {
                    "login": bug['owner'] if bug['owner'] != "" else None
                },
                "reporter": {
                    "login": bug['originator']
                },
                "state": "closed" if bug['done'] != "" else "open"
            }
            self.save_bug(bugobj)


    def update(self):
        log("Getting open bugs")
        self._import_bugs("package", self._package, "status", 'open')
        log("Getting done bugs")
        self._import_bugs("package", self._package, 'status', 'done')
