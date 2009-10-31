#!/usr/bin/env python
# Created By: Virgil Dupras
# Created On: 2009-10-31
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

import os
import os.path as op

from hsutil.build import print_and_do, build_all_qt_ui

build_all_qt_ui(op.join('qtlib', 'ui'))
build_all_qt_ui('ui')

# os.chdir('help')
# print_and_do('python gen.py')
# os.chdir('..')