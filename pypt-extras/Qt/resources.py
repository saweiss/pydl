# -*- encoding: utf-8 -*-
# PyDL v0.1.0
# IDL functionality in Python
# Copyright © 2018, Samuel A. Weiss.
# See /LICENSE for licensing information.
# This file was adapted from Chris Warrick’s Python Project Template.

"""
Adapt Qt resources to Python version.

:Copyright: © 2018, Samuel A. Weiss.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import sys

if sys.version_info[0] == 2:
    import pydl.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import pydl.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
