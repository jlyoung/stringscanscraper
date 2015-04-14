import argparse
import re
import sys
import urllib2
from bs4 import BeautifulSoup

def contains_match(search_term, host):
	target_url = urllib2.urlopen(host)
	target_url_content = target_url.read()
	page_content = BeautifulSoup(target_url_content)
	prog = re.compile(search_term,flags=re.IGNORECASE)
	found = []
	for text in page_content.stripped_strings:
		if prog.search(text):
			found.append(text)
	return found
	

def main():
	parser = argparse.ArgumentParser(description='Search a list of urls for search terms.')
	parser.add_argument('--searchterm', '-s', metavar='TERM_TO_SEARCH',
						help='The term to search for')
	parser.add_argument('--urls', '-u', metavar='URLS', nargs='+',
						help='The term to search for')
	args = parser.parse_args()
	search_term = args.searchterm
	hosts = args.urls
	for host in hosts:
		try:
			found = contains_match(search_term, host)
			if contains_match(search_term, host):
				print "Host '{host}' contains the search term '{search_term}'".format(host=host, search_term=search_term)
				for entry in found:
					print "\t"+entry
			else:
				print "Host '{host}' DOES NOT contain the search term '{search_term}'".format(host=host, search_term=search_term)
		except:
			print "Unexpected error:", sys.exc_info()[0]


if __name__ == '__main__':
	main()