from tweetpie.core import Twitter, TwitterError, Error, ENDPOINTS, AuthError,\
                     ParamError
import nose
t = Twitter()

#--------------------Tests-----------------------------------------------#
def test_call_geo_search_ip():
    """ Test for params ip in geo_search. This ip address belongs to tumblr"""
    r = t.call('geo_search', params={'ip': '66.6.44.4'})
    assert r['result']['places'][1]['name'] == u'Manhattan'

def test_call_geo_search_query_toronto():
    """ Test for params query in geo_search. query = Toronto """
    r = t.call('geo_search', params={'query': 'Toronto'})
    assert r['result']['places'][1]['name'] == u'Toronto'

def test_call_geo_search_query_bangalore():
    """ Test for params query in geo_search. query = Bangalore
    Shame on twitter don't Bangalore ?
    """
    r = t.call('geo_search', params={'query': 'Bangalore'})
    assert r['result']['places'] == []

def test_get_func_names():
    r = t.get_func_names()
    assert len(r) >= 1

def test_get_func_details():
    r = t.get_func_details('geo_search')
    nose.tools.assert_is_instance(r, str)
