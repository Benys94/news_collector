#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <dbenes@netsuite.com>
.. Created on 2019-06-15
"""

import sys
from os.path import abspath, dirname, join, pardir

sys.path.append(join(abspath(dirname(__file__)), pardir))

from src.api_interface import APIHandler, NewStoriesAPI


def parse_response(response_data):
    """
    Process response from web API

    :param dict response_data:
        Raw json data returned by web API
    """
    print(len(response_data), response_data)


if __name__ == '__main__':
    API_CLIENT = APIHandler(
        worker=NewStoriesAPI(),
        address='hacker-news.firebaseio.com/v0',
        schema='https'
    )
    RES_DATA = API_CLIENT.get_api_data()
    parse_response(RES_DATA)
