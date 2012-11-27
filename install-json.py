#!/usr/bin/python
import json
import getopt
import sys
from pprint import pprint

termWidth = 80

checkOnly = False
verbose = False
force = False

def main():
	global checkOnly
	global verbose
	global force
	try:
		opts, args = getopt.getopt(sys.argv[1:], "cvf", ["file=", "verbose", "check", "force-install"])
	except getopt.GetoptError, err:
		print str(err)
		sys.exit(2)

	filename = 'packages.json';

	for o, a in opts:
		if o in ("-c", "--check"):
			checkOnly = True
		if o in ("-v", "--verbose"):
			verbose = True
		if o in ("-f", "--force-install"):
			force = True
		if o in ("--file"):
			force = True
			filename = a;

	data = json.load(open(filename))

	for item in data['packages']:
		install(item)

def install(item):
	if item['type'] == "apt-get":
		install_AptGet(item)

def install_AptGet(item):
	if item.has_key('check'):
		# temp is used to get the chars remaining
		temp = "Checking for " + item['name']
		print temp

		runCommand(item['check'], termWidth - len(temp))
	else:
		print "run regular check"
	pprint(item)

def runCommand(cmd, dotsLeft):
	print "running ", cmd

if __name__ == "__main__":
	main()
