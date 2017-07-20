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

#The main function starts...
def main():
	# The main function

	# Check Balance
	if args.balance is True:
		bal = api.balance(username, password)
		print('\nCurrent Balance: ', bal[0:])
	
	# Send a short SMS
	if args.text is True:
		text = message()
		gsm = number()
		print('\nSMS Text: ', text, '\nReciever: ', gsm, '\n\nEnter y or Y to Confirm, n or N to discard: ')
		verify = str(input())
		if verify == 'y' or verify == 'Y':
			url = api.s_sms(username, password, text, gsm)
			if url is not None:
				print('\nSMS Send Success...\nID: ',url)
				sys.exit()
		else:
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
