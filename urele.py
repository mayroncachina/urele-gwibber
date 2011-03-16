"""
Urele interface for Gwibber
Mayron Cachina  - 10/21/2010
http://cachina.com.br

"""

import urllib2

PROTOCOL_INFO = {

  "name": "urele",
  "version": 0.1,
  "fqdn" : "http://urele.com",
  
}

class URLShorter:

  def short(self, text):
    short = urllib2.urlopen("http://urele.com/api/create_url?url=%s" % urllib2.quote(text)).read()
    return short

