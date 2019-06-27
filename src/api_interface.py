#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <benys94@gmail.com>
.. Created on:: 2019-06-16
"""

import logging
import requests
from abc import ABC, abstractmethod


class BaseSender(ABC):
    """Sending a HTTP requests to certain web pages"""

    @abstractmethod
    def send_req(self, path, payload=None):
        """
        Method to be implemented in all subclasses.
        It sends given payload data to given web API

        :param str path:
            API path to be reached
        :param payload:
            Request data to be sent
        :return:
            Service's response
        """


class NewStoriesAPI(BaseSender):
    """Get list of IDs pointing to new articles"""

    def send_req(self, path, payload=None):
        """
        Implementation of :meth:`src.api_interface.BaseSender.send_req`
        """
        full_path = "{url}/newstories.json".format(url=path)
        return requests.get(full_path, payload).json()


class APIHandler:
    """
    Handle all API communication with external services

    :param BaseSender worker:
        Worker to be used for new instance of this class
    :param str address:
        URL of web service
    """

    def __init__(self, worker, address):
        self._logger = logging.getLogger(self.__class__.__name__)
        self.worker = worker
        self._api_address = address

    def get_api_data(self, payload=None):
        """
        Prepare data and send request to external API

        :param payload:
            Data to be sent API service
        :return:
            API response
        """
        self._logger.info('Sending request to %s', self._api_address)
        return self.worker.send_req(self._api_address, payload)
