#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <benys94@gmail.com>
.. Created on:: 2019-06-16
"""

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
    :param int port:
        Port of web service. This argument is optional
    :param str schema:
        Schema of web service. HTTP is default
    """

    def __init__(self, worker, address, port=None, schema="http"):
        self.worker = worker
        tmp_port = ":{}".format(port) if port is not None else ""
        self._api_address = "{schema}://{address}{port}".format(
            schema=schema, address=address, port=tmp_port
        )

    def get_api_data(self, payload=None):
        """
        Prepare data and send request to external API

        :param payload:
            Data to be sent API service
        :return:
            API response
        """
        return self.worker.send_req(self._api_address, payload)
