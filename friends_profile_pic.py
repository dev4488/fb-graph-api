#Downloads all the profile_pics of your friends on facebook
#by: Devinder Kumar 
#email: devinderkumar[AT]ieee[DOT]org

import requests
import json
import urllib

TOKEN = '<your access token here>'    #enter your access_token which can be obtained from Graph API Explorer

def get_profile_pic():
    #returns a dict of url of all the profile pics of your friend on facebook
    query = ("SELECT pic FROM user WHERE uid IN  (SELECT uid2 FROM friend WHERE uid1 = me() ) LIMIT 1000")
    payload = {'q':query,'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def save_photos(photos):         #downloads all the pics in 
    count = 0
    for photo in photos:
        count+=1
        print "succesfully downloaded cover_pic_%s" % count,photo['pic']
        urllib.urlretrieve(photo['pic'],"pic%s" %count)

if __name__ == '__main__':
	save_photos(get_profile_pic())

