# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the
# terms and conditions of the Expat license.

def create_id(prefix, klass, package, idno):
    return "%s-%s-%s-%s" % (
        prefix,
        klass,
        package,
        idno
    )
