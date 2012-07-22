# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under
# the terms and conditions of the Expat license

from organized.importer import Importer

class GitHub(Importer):
    def __init__(self, owner, project):
        self._owner = owner
        self._project = project

    def update(self):
        pass
