import requests
import json
import urllib

TOKEN = '<your access token here>'

def get_url():
    #returns a dict of url of all pics of facebook logged in account
    query = ("SELECT src FROM photo_src WHERE photo_id IN (SELECT object_id FROM photo WHERE aid IN (SELECT aid FROM album WHERE owner = me()))""AND width < 100 LIMIT 1000")
    
    payload = {'q':query,'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def save_pics(urls):
    count = 0
    
    for url in urls:
        count+=1
        print "succesfully downloaded pic_%s" % count,url['src']
        urllib.urlretrieve(url['src'],"pic%s" %count)

if __name__ == '__main__':
	save_pics(get_url())

