#Downloads all the photos of your friends on facebook
#by: Devinder Kumar 
#email: devinderkumar[AT]comsoc[DOT]org

import requests
import json
import urllib

TOKEN = '<your access_token here>'

def get_photos():
    #returns a dict of url of photos in your friend's visble albums #change width to get different sizes of pics
    query = ("SELECT src FROM photo_src WHERE photo_id IN (SELECT object_id FROM photo WHERE aid IN (SELECT aid FROM album WHERE owner IN (SELECT uid2 FROM friend WHERE uid1= me())))""AND width > 1000  LIMIT 1000")

    payload = {'q':query,'access_token': TOKEN}
    response = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(response.text)
    return result['data']

def save_photos(photos):
    #saves all the photos
    counter = 0
    for photo in photos:
        counter +=1
        print "successfully downloaded pic_%s " % counter
        urllib.urlretrieve(photo['src'],"pic_%s" %counter)


if __name__ == '__main__':
	save_photos(get_photos())
