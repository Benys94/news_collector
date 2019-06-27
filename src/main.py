#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <dbenes@netsuite.com>
.. Created on 2019-06-15
"""

import logging
import sys
from os.path import abspath, dirname, join, pardir

sys.path.append(join(abspath(dirname(__file__)), pardir))

from src.api_interface import APIHandler
from src.options import OPTIONS


def get_cfg(cfg_label, cfg_dict):
    """
    Get requested configuration from given dictionary or raise an exception.

    :param cfg_label:
        Label of configuration to get
    :param dict cfg_dict:
        Dictionary with all configurations available
    :raises: At
    :return: Config from given structure
    :rtype: dict
    """
    tmp_cfg = cfg_dict.get(cfg_label)
    if tmp_cfg is None:
        raise AttributeError("No configuration for '{}'".format(cfg_label))
    return tmp_cfg


class Runner:
    """Base class for this whole service."""

    def __init__(self, **kwargs):
        self._logger = logging.getLogger(self.__class__.__name__)
        api_cfg = get_cfg('api_services', kwargs)

        stories_cfg = get_cfg('new_stories', api_cfg)
        self.stories_api = APIHandler(**stories_cfg)

    def get_stories(self):
        """Get all new stories"""
        response_data = self.stories_api.get_api_data()
        self._logger.info("%d records: %s", len(response_data), response_data)


if __name__ == '__main__':
    logging.basicConfig(**OPTIONS['logger'])
    try:
        RUNNER = Runner(**OPTIONS)
        RUNNER.get_stories()
    except KeyboardInterrupt:
        logging.error("Service terminated")
    except Exception as e_msg:
        logging.error('Unhandled exception')
        logging.exception(e_msg)
