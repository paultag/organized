# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the
# terms and conditions of the Expat license.

from pymongo import Connection

connection = Connection('localhost', 27017)
db = connection.organized
