# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log
import SOAPpy

url = 'http://bugs.debian.org/cgi-bin/soap.cgi'
namespace = 'Debbugs/SOAP'
server = SOAPpy.SOAPProxy(url, namespace)


class BTS(Importer):
    def __init__(self, package, root_project):
        log("Created bts instance. %s" % (
            package
        ))
        self._package = package
        self.__init(root_project)


    def _import_bugs(self, *args):
        bugs = server.get_bugs(*args)
        objs = server.get_status(bugs)['item']
        for bug in objs:
            bug = bug['value']


    def update(self):
        self._import_bugs("package", self._package)
