#script to download the xkcd comics
#TODO:comment code, add sys.argv input method

import os
import sys
import requests
import urllib
from BeautifulSoup import BeautifulSoup

def input_param():
	try:
		start = int(raw_input("enter starting comic page no.: "))
		end =   int(raw_input("enter last comic page no. : "))
	except ValueError:
		sys.exit ("Exiting program... \nError Message: enter numerical values for start:end range")
	if (start > end or start<1 or end <1):
		sys.exit("Exiting program... \nError Message: enter valid start:end range")
	return start,end

def get_url(start,end):
	list_url=[]
	print "fetching urls..."
	for comic_num in range(start,end+1):
		page = "http://xkcd.com/%s" %comic_num
		url = requests.get(page)
		html = url.text
		soup = BeautifulSoup(html)
		for link in soup.findAll("div",{"id":"comic"}):
			list_url.append(link.find("img")['src'])
	return list_url

def download_comic(urls):
	count = start
	for url in urls:
		print "downloading xkcd_%s ..." % count
		urllib.urlretrieve(url,"xkcd_%s" % count)
		count+=1

if __name__ == '__main__':
	current_dir = os.getcwd()
	path = current_dir+"/xkcd"
	start,end = input_param()
	if not os.path.exists(path):
		os.makedirs(path)
		os.chdir(path)
		download_comic(get_url(start,end)) 

	else:
		os.chdir(path)
		download_comic(get_url(start,end))
