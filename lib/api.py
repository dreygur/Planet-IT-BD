#!/usr/bin/env python

#############################################################################
#    PLanet IT API - Python 3.6 Planet IT API.
#    Copyright (C) 2017 by Rakibul Yeasin Totul
#    URI - https://www.rytotul.xyz/about
#	 Facebook - https://www.facebook.com/rytotul
#	 Github - https://www.github.com/rytotul
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#############################################################################

import sys
from urllib import request as req
from urllib import parse as prs


class PlanetError(RuntimeError):
    """Planet IT API error.

    The error message returned by the web application is stored as the Python 
    exception message."""


class PlanetAPI(object):

    # String to determine bad API requests
    _bad_request = 'Bad API request'

    # Base domain name
    _base_domain = 'app.planetgroupbd.com'

    # URL to the Short SMS API
    _api_short_sms_url = 'http://%s/api/sendsms/plain' % _base_domain

    # URL to the Long SMS API
    _api_long_sms_url = 'http://%s/api/v3/sendsms/plain' % _base_domain

    # URL to the Sheduled SMS API
    _api_shedule_sms_url = 'http://%s/api/v3/sendsms/plain' % _base_domain

    # URL to the Unicode SMS API
    _api_uni_sms_url = 'http://%s/api/v3/sendsms/plain' % _base_domain

    # URL to the Unicode-Binary SMS API
    _api_uni_sms_bin_url = 'http://%s/api/v3/sendsms/plain' % _base_domain

    # URL to the Balance Check API
    _api_balance_url = 'http://%s/api/command/?' % _base_domain

    # URL to the Delevery Report API
    _api_uni_sms_bin_url = 'http://%s/api/dr/pull' % _base_domain


    def __init__(self):
        pass


    def balance(self, api_user, api_pass):
        # We can retrieve our remaining credit balance with this function
        # We will make a Dictionary with all the Data
        _argv = {'user' : str(api_user),
                 'password' : str(api_pass),
                 'cmd' : 'Credits'}

        # Base url for Checking Balance
        url = 'http://app.planetgroupbd.com/api/command/?'
        # encoding the Data as url
        enc_url = prs.urlencode(_argv)
        # joining base url and encoded url
        request = url + enc_url
        # opening the url
        result = req.urlopen(request)
        # converting the result to string
        response = str(result.read())
        # filtering unusable things
        response = response[2:]
        response = response[:-1]

        return response

    def s_sms(self, api_user, api_pass, api_text, api_gsm):
        # We can retrieve our remaining credit balance with this function
        # We will make a Dictionary with all our Data
        _argv = {'user' : str(api_user),
                 'password' : str(api_pass),
                 'sender' : 'Totul',
                 'SMSText' : str(api_text),
                 'GSM' : str(api_gsm)}

        # Base url to send a short SMS
        url = 'http://app.planetgroupbd.com/api/sendsms/plain/?'
        # encoding the Data as url
        enc_url = prs.urlencode(_argv)
        # joining base url and encoded url
        request = url + enc_url
        # opening the url to run the commands
        result = req.urlopen(request)
        response = str(result.read())
        # filtering unusable things
        response = response[2:]
        response = response[:-1]
        return response


######################################################

_api = PlanetAPI()
#short_sms = _api.short_sms
balance = _api.balance
"""
username = 'khansunny245'
password = '01768072680'
balance(username, password)
"""
short = _api.s_sms
"""
sender = 'Khan Sunny'
text = 'Hi Totul...'
gsm = '8801710909755'
res = short(username, password, sender, text, gsm)
print(res)
"""

######################################################
