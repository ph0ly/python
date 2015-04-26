#!/usr/bin/python
# -*- coding: utf-8 -*-

'A Http Client implements v1.0.0'

__author__ = 'pholy.ht'
__time__ = '2015-04-26'

import httplib
import urllib


class HttpClient:
    def __init__(self):
        pass

    def get(self, url, *args, **kw):
        return self.__get(url, 'GET', *args, **kw)

    def post(self, url, *args, **kw):
        return self.__get(url, 'POST', *args, **kw)

    def put(self, url, *args, **kw):
        return self.__get(url, 'PUT', *args, **kw)

    def delete(self, url, *args, **kw):
        return self.__get(url, 'DELETE', *args, **kw)

    def __get(self, url, method, *args, **kw):
        conn = self.__open_connection(self.__get_root_path(url))
        req_url = self.__get_path_context(url)
        if req_url.__contains__('?'):
            req_url += '&' + self.__generate_url_params(*args, **kw)
        else:
            req_url += '?' + self.__generate_url_params(*args, **kw)
        print req_url
        conn.request(method, req_url)
        result = conn.getresponse().read()
        conn.close()
        return result

    # def post(self, url, *args, **kw):
    #     conn = self.__open_connection(self.__get_root_path(url))
    #     req_url = self.__get_path_context(url)
    #     print self.__generate_body_params(*args, **kw)
    #     req_url += "?" + self.__generate_body_params(*args, **kw)
    #     conn.request('POST', req_url)
    #     result = conn.getresponse().read()
    #     conn.close()
    #     return result
    #
    # def put(self, url, *args, **kw):
    #     conn = self.__open_connection(self.__get_root_path(url))
    #     req_url = self.__get_path_context(url)
    #     conn.request('PUT', req_url, body=self.__generate_body_params(*args, **kw))
    #     result = conn.getresponse().read()
    #     conn.close()
    #     return result
    #
    # def delete(self, url, *args, **kw):
    #     conn = self.__open_connection(self.__get_root_path(url))
    #     req_url = self.__get_path_context(url)
    #     if req_url.__contains__('?'):
    #         req_url += '&' + self.__generate_url_params(*args, **kw)
    #     else:
    #         req_url += '?' + self.__generate_url_params(*args, **kw)
    #     conn.request('DELETE', req_url)
    #     result = conn.getresponse().read()
    #     conn.close()
    #     return result

    def __open_connection(self, url):
        return httplib.HTTPConnection(url)

    def __generate_url_params(self, *args, **kw):
        params = ''
        if args.__len__() % 2 != 0:
            raise 'invalid http params, expected even count!'
        for i in [x for x in range(0, args.__len__()) if x % 2 == 0]:
            params = params + args[i] + '=' + args[i+1] + '&'
        for k, v in kw.iteritems():
            params = params + k + '=' + v + '&'
        return params

    def __generate_body_params(self, *args, **kw):
        params = {}
        if args.__len__() % 2 != 0:
            raise 'invalid http params, expected even count!'
        for i in [x for x in range(0, args.__len__()) if x % 2 == 0]:
            params[args[i]] = args[i+1]
        for k, v in kw.iteritems():
            params[k] = v
        return urllib.urlencode(params)

    def __get_root_path(self, url):
        if url.__contains__('http://'):
            a, url = url.split('http://', 1)
        if url.__contains__('/'):
            root_path, context = url.split('/', 1)
            return root_path
        else:
            return url

    def __get_path_context(self, url):
        if url.__contains__('http://'):
            a, url = url.split('http://', 1)
        if url.__contains__('/'):
            root_path, context = url.split('/', 1)
            return '/' + context
        else:
            return '/'




