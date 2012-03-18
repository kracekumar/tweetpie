#! /usr/bin/env python
#! -*- coding: utf-8 -*-

#---------------------- CONSTANTS ---------------------------#
AUTHENTICATED_RATE_LIMIT = 350
UNAUTHENTICATED_RATE_LIMIT = 150

#---------------------ENDPOINTS with URL in DICTIONARY ------#
ENDPOINTS = {'authenticate': {
                                'authentication_required': True,
                                'url': \
                                'https://api.twitter.com/oauth/authenticate',
                                'method': 'GET',
                                },
             'geo_search': {
                                'authentication_required': False,
                                'url':\
                                'https://api.twitter.com/1/geo/search.json',
                                'method': 'GET',
                                'func_doc': 
                                """
                                    geo_search
                                    ----------
                                    returns json details for mentioned geo 
                                    specic details

                                    params
                                    ------
                                    At least one of the following parameters 
                                    must be provided to this resource: 
                                    lat, long, ip, or query

                                    :lat: The latitude to search around. 
                                     This parameter will be ignored unless it is
                                     inside the range -90.0 to +90.0 
                                     (North is positive) inclusive. 
                                     It will also be ignored if there 
                                     isn't a corresponding long parameter.

                                     E.G: lat = 37.7821120598956

                                     :long: The longitude to search around. 
                                      The valid ranges for longitude is -180.0 
                                      to +180.0 (East is positive) inclusive. 
                                      This parameter will be ignored if outside 
                                      that range, if it is not a number, 
                                      if geo_enabled is disabled, or if there 
                                      not a corresponding lat parameter.

                                     E.G: long: -122.400612831116

                                     :query: Free-form text to match against 
                                      while executing a geo-based query, best 
                                      suited for finding nearby locations by 
                                      name.

                                     E.G: query='Twitter%20HQ'

                                     :ip: An IP address. Used when attempting 
                                     to fix geolocation based off of the user's 
                                     IP address.

                                     E.G: 74.125.19.104

                                     Usage
                                     -----
                                     t = Twitter()
                                     print t.call(func_name='geo_search', 
                                           params={'query': 'Toronto'})
                                """,
                                'required_params': ['lat', 'long', 'ip', 'query'],
                                'required_params_choice': True,
                                'doc_link': 'https://dev.twitter.com/docs/api/1/get/geo/search'
                                },
             'geo_reverse_geocode':{                   
                                    'authentication_required': False,
                                    'method': 'GET',
                                    'url': "https://api.twitter.com/1/geo/reverse_geocode.json",
                                    'required_params': ['lat', 'long'],
                                    'required_params_choice': False,
                                    'doc_link': "https://dev.twitter.com/docs/api/1/get/geo/reverse_geocode",
                                    'func_doc': """
                                                geo_reverse_geocode
                                                -------------------
                                                Given a latitude and a longitude
                                                , searches for up to 20 places 
                                                that can be used as a place_id 
                                                when updating a status.

                                                params
                                                ------
                                                Mandatory
                                                ---------

                                                :lat: The latitude to search 
                                                 around. This parameter will be 
                                                 ignored unless it is inside the
                                                 range -90.0 to +90.0 (North is 
                                                 positive) inclusive. 
                                         
                                                 It will also be ignored if 
                                                 there isn't a corresponding 
                                                 long parameter.

                                                 E.G: lat=-22.400612831116

                                                 :long: The longitude to search 
                                                  around. The valid ranges for 
                                                  longitude is -180.0 to +180.0
                                                  (East is positive) inclusive.
                                                  
                                                  This parameter will be ignored 
                                                  if outside that range, if it 
                                                  is not a number, if 
                                                  geo_enabled is disabled, or 
                                                  if there not a corresponding 
                                                  lat parameter.

                                                  E.G long: -122.4006

                                                  More docs 
                                                  ---------
                                                  https://dev.twitter.com/docs/
                                                  api/1/get/geo/reverse_geocode
                                                  
                                                  Usage
                                                  -----
                                                  t = Twitter()
                                                  print t.call(
                                                  func_name='geo_search', 
                                                  params={'query': 'Toronto'})


                                                """
                                    }}
