#! /usr/bin/env python
#! -*- coding: utf-8 -*-
#-----------------------------------Import-----------------------------------#
try:
    import requests
    import oauth_hook
except ImportError:
    raise Exception("Install \
                    requests: http://pypi.python.org/pypi/requests/0.10.2 \
                    requests-oauth: http://pypi.python.org/pypi/requests-oauth/\
                    0.3.0")

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise Exception("Install \
                       simplejson:http://pypi.python.org/pypi/simplejson/2.3.2")

from constants import ENDPOINTS

class TwitterError(requests.RequestException):
     """
        Entire error handling, we are standing on requests shoulder.
     """
     def __init__(self, error):
         self._error_message = error.message

     def __str__(self):
         return repr(self._error_message)

class Error(Exception):
    """
        class to handle other exceptions like keyboard interrupt, KeyError etc..

    """
    def __init__(self, error):
        self._error_message = error.message

    def __str__(self):
       return repr(self._error_message)

class AuthError(Error):
    """
        Class to handle authentication error
    """
    def __init__(self, error):
        self._error_message = error.message

    def __str__(self):
       return repr(self._error_message)

class ParamError(Error):
    """
        Class to handle authentication error
    """
    def __init__(self, error):
        self._error_message = error.message

    def __str__(self):
       return repr(self._error_message)


class Twitter(object):
     """ This is base class """
     def __init__(self):
         self._access_token = False
         self._access_token_secret = False
         self._consumer_key = False
         self._consumer_secret = False
         self._is_authenticated = False
         self._client = None
         self._oauth_hook = None

     def set_tokens(self, access_token, access_token_secret, consumer_key,\
                     consumer_secret):
         """ set tokens when ever you wish """
         self._access_token = access_token
         self._access_token_secret = access_token_secret
         self._consumer_key = consumer_key
         self._consumer_secret = consumer_secret
         self._oauth_hook =  oauth_hook.OAuthHook(self._access_token, \
                             self._access_token_secret, self._consumer_key,\
                             self._consumer_secret)

     @property
     def oauth_hook(self):
         return self._oauth_hook

     def authenticate(self):
         """ Use this function when you need user to authenticate into your site
         """
         if self._access_token and self._access_token_secret and \
            self._consumer_key and self._consumer_secret:
            try:
                self._client = requests.session(hooks=\
                               {'pre-request': self._oauth_hook})
                self.r =  self._client.get(ENDPOINTS['authenticate']['url'])
                self.r.raise_for_status()
                self._is_authenticated = True
                return self.r

            except KeyError as e:
                raise Error(e)

            except requests.HTTPError as e:
                raise TwitterError(e)

     def get_func_names(self):
         """
            Returns list of all func names, similar to --help in command line 
         """
         return ENDPOINTS.keys()
     
     def get_func_details(self, func_name):
         """
            Return details like function url, function method, description and 
            other relevant details
         """
         try:
             msg = []
             if ENDPOINTS[func_name]:
                for key in ENDPOINTS[func_name]:
                   msg.append("%s: %s"%(key, ENDPOINTS[func_name][key]))
             return ', '.join(msg)
         except KeyError:
             return "Function name is not found, try get_func_names()"
         
     def call(self, func_name, **kwargs):
         """
            params
            ------
            : func_name => name of the func to be called, 
              E.G func_name = 'search'
            
            : param: dict to be passed, depends on func.

            Note
            ----
            In order to get details of a func
            t = Twitter()
            print t.get_func_names()
            print t.get_func_details('search')
         """
         try:
            d = ENDPOINTS[func_name]
            if d['required_params']:
                """
                    some functions requires compulsory params, checking for that
                """
                if kwargs['params']:
                    required_params = set(d['required_params'])
                    params = set(kwargs['params'])
                    r = required_params and params
                    if d['required_params_choice']:
                        if len(r) <1:
                            keys = ", ".join(required_params)
                            msg = keys + "any one of the params is required"
                            e = Exception()
                            e.message = msg
                            raise ParamError(e)
                    else:
                        if len(r) is not len(required_params):
                            e = Exception()
                            items = ", ".join(d['required_params'])
                            e.message = " %s all of the param is required"\
                                        %(items)
                            raise ParamError(e) 
                else:
                    e = Exception()
                    items = ", ".join(d['required_params'])
                    print items
                    e.message = " %s any one of the param is required"\
                                %(items)
                    raise ParamError(e)

            if d['authentication_required']:
                if self._is_authenticated:
                    self._client = requests.session(hooks={'pre-request':\
                                                           self._oauth_hook})
                    if d['method'] is 'GET':
                        r = self._client.get(d['url'], params=kwargs['params'])
                        r.raise_for_status()
                    if d['method'] is 'POST':
                        r = self._client.get(d['url'], params=kwargs['params'])
                        r.raise_for_status()
                    s = r.headers.get('content-type')
                    if s.find('json') >= 0:
                        return json.loads(r.content)
                    else:
                        return r
                else:
                    raise AuthError("Authentication is required,\
                                    use authenticate() or authorize() function\
                                    and then call this function")
            else:
                if d['method'] is 'GET':
                    r = requests.get(d['url'], params=kwargs['params'])
                    r.raise_for_status()
                elif d['method'] is 'POST':
                    r = requests.post(d['url'], params=kwargs['params'])
                    r.raise_for_status()
                s = r.headers.get('content-type')
                if s.find('json') >= 0:
                    return json.loads(r.content)
                else:
                    return r
                
         except KeyError as e:
             e.message = "%s not found, use get_func_names() "%e.args
             raise Error(e)

         except requests.HTTPError as e:
             raise TwitterError(e)


         




    
