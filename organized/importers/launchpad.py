# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer
from organized.util import create_id, log

from launchpadlib.launchpad import Launchpad

launchpad = Launchpad.login_anonymously('paultag', 'production')
PREFIX = 'launchpad'

class Launchpad(Importer):
    def __init__(self, project, root_project):
        log("Created launchpad instance. %s" % (
            project
        ))
        self._project = project
        self._init(root_project)


    def _process_project(self, **kwargs):
        project = launchpad.projects[self._project]
        bugs = project.searchTasks(**kwargs)
        for bug in bugs:
            print bug


    def update(self):
        for status in [ 'New', 'Incomplete', 'Opinion', 'Invalid', "Won't Fix",
                        'Expired', 'Confirmed', 'Triaged', 'In Progress',
                        'Fix Committed', 'Fix Released',
                        'Incomplete (with response)',
                        'Incomplete (without response)' ]:
            self._process_project(status=status)
