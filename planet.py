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

# importing modules
import sys
sys.dont_write_bytecode = True

from optparse import OptionParser
from lib.api import PlanetAPI

# Calling from modules...
parser = OptionParser()
api = PlanetAPI()

# Parser options...
parser.add_option("-t", "--text", help="To send a short SMS", default="Command to send a short SMS", action="store_true")
parser.add_option("-b", "--balance", help="Command to check the current balance", action="store_true")

# Gathering all parser-options in a variable
(args, _) = parser.parse_args()

# App api and login informations
username = ''									# Your username
password = ''									# Your Password

# User Input Message
def message():
	print('\nEnter your Message:')
	text = str(input())
	return text

# User Input Phone number
def number():
	print('\nEnter the phone number where to send SMS:')
	gsm = str(input())
	return gsm

def sms_check(res):

    	if res == '0':
    		response = 'Request was Succesfull'
    	elif res == '-1':
    		response = 'Error proccessing the request'
    	elif res == '-2':
    		response = 'You don\'t have enough credits...'
    	elif res == '-3':
    		response = 'Currenty we can\'t send SMS to this network.'
    	elif res == '-5':
    		response = 'Username or Password is invalid'
    	elif res == '-6':
    		response = 'Destination address is missing'
    	elif res == '-10':
    		response = 'Missing username'
    	elif res == '-11':
    		response = 'Missing the password'
    	elif res == '-13':
    		response = 'Number is not recognised. \nPlease make sure you have added 88 before the number'
    	elif res == '-34':
    		response = 'Sender ID is not Valid'
    	elif res == '-99':
    		response = 'Error proccessing request'
    	else:
    		response = 'SMS send success. ID: ' + res

    	return response

#The main function starts...
def main():
	# The main function

	# Check Balance
	if args.balance is True:
		bal = api.balance(username, password)
		ans = sms_check(bal)
		print('\nCurrent Balance: ', ans)
	
	# Send a short SMS
	if args.text is True:
		text = message()
		gsm = number()
		print('\nSMS Text: ', text, '\nReciever: ', gsm, '\n\nEnter y or Y to Confirm, n or N to discard: ')
		verify = str(input())
		if verify == 'y' or verify == 'Y':
			response = api.s_sms(username, password, text, gsm)
			ans = sms_check(response)
			print('\n', ans)
			sys.exit()

# Starting the program from here...
if __name__ == "__main__":
	try:
		main()
	except IOError:
		print ('\nNot connected to Internet. Connect to internet first...')
		sys.exit()
		pass

# end..............................................
