#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. codeauthor:: David Benes <dbenes@netsuite.com>
.. Created on 2019-06-15
"""

import requests


class RequestSender:
    """
    Sending a HTTP requests to certain web pages

    :param str address:
        URL of web service
    :param int port:
        Port of web service. This argument is optional
    :param str schema:
        Schema of web service. HTTP is default
    """

    def __init__(self, address, port=None, schema="http"):
        tmp_port = ":{}".format(port) if port is not None else ""
        self._api_address = "{schema}://{address}{port}".format(
            schema=schema, address=address, port=tmp_port
        )

    def send_req(self, path, payload=None):
        """
        Sends given data to web API

        :param str path:
            API path to be reached
        :param payload:
            Data to be sent
        :return:
            Service's response
        :rtype: dict
        """
        full_path = "{url}/{path}".format(
            url=self._api_address, path=path
        )
        response = requests.get(full_path, payload)
        return response.json()


def parse_response(response_data):
    """
    Process response from web API

    :param dict response_data:
        Raw json data returned by web API
    """
    print(len(response_data), response_data)


if __name__ == '__main__':
    API_CLIENT = RequestSender(
        address='hacker-news.firebaseio.com/v0',
        schema='https'
    )
    RES_DATA = API_CLIENT.send_req(path='newstories.json')
    parse_response(RES_DATA)
