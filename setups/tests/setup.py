#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from setuptools import setup

setup(
    name="naruno_tests",
    version="0.44.4",
    description="""This is a tool for tests on Naruno""",
    url="https://docs.naruno.org/",
    author="Naruno Developers",
    author_email="onur.atakan.ulusoy@naruno.org",
    license="MPL-2.0",
    install_requires="""
requests==2.28.0
pytest==7.1.2
speed_calculator==0.4.1
naruno_api==0.44.4
""",
    python_requires=">=3.8",
    zip_safe=False,
)
