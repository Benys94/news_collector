#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <benys94@gmail.com>
.. Created on 2019-06-27
"""

import logging
import sys
from os.path import abspath, dirname, join, pardir

sys.path.append(join(abspath(dirname(__file__)), pardir))

from src.api_interface import NewStoriesAPI


OPTIONS = {
    'logger': {
        'stream': sys.stderr,
        'filemode': 'a',
        'level': logging.DEBUG,
        'datefmt': '%Y-%m-%d %H:%M:%S',
        'format': (
            '%(asctime)s - %(levelname)s: %(name)s - %(message)s; '
            '%(funcName)s:%(lineno)s'
        )
    },

    'api_services': {
        'new_stories': {
            'worker': NewStoriesAPI(),
            'address': 'https://hacker-news.firebaseio.com/v0'
        }
    }
}
