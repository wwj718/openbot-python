# -*- coding: utf-8
import requests
import logging


DEFAULT_VERSION = '20161103'
BASE_URL = "openbot.just4fun.site" # 127.0.0.1


class OpenBotError(Exception):
        pass

def req(host,logger, access_token, meth, path, params, **kwargs):
    '''
    meth : http methord
    '''
    full_url = host + path
    logger.debug('%s %s %s', meth, full_url, params)
    # use log to debug
    print(full_url)
    headers = {
        'authorization': 'Bearer ' + access_token,
        'accept': 'application/json'
    }
    headers.update(kwargs.pop('headers', {}))
    rsp = requests.request(
        meth,
        full_url,
        headers=headers,
        params=params,
        **kwargs
    )
    if rsp.status_code > 200:
        raise OpenBotError('openbot responded with status: ' + str(rsp.status_code) +
                       ' (' + rsp.reason + ')') # todo format
    json = rsp.json() # error in response
    if 'error' in json:
        raise OpenBotError('openbot responded with an error: ' + json['error'])

    logger.debug('%s %s %s', meth, full_url, json)
    return json


class OpenBot(object):
    """
        Main endpoint for using openbot.just4fun.site (demo)
        Provides request.
        Basic Usage::
            >>> ...
            >>> import openbot
            >>> ai = openbot.OpenBot(<CLIENT_ACCESS_TOKEN>)
            >>> text_request = ai.text_request()
            >>> ...
        :param client_access_token: client access token provided by http://openbot.just4fun.site
        :type client_access_token: str or unicde
    """
    def __init__(self,host, client_access_token, session_id=None, logger=None):
        super(OpenBot, self).__init__()
        self._client_access_token = client_access_token
        self._host = host
        self._version = DEFAULT_VERSION
        self.logger = logger or logging.getLogger(__name__) # set log

    def chat(self, query, context=None, verbose=None):
        params = {}
        params["query"] = query
        resp = req(self._host,self.logger, self._client_access_token, 'GET', '/openbot/chat', params)
        return resp

    def train(self, dialogue, context=None, verbose=None):
        '''
        dialogue split with space
        '''
        params = {}
        params["corpus_strings"] = dialogue
        resp = req(self._host,self.logger, self._client_access_token, 'POST', '/openbot/chat', params)
        return resp
