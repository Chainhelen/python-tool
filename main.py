import header
import requests
import sys
from pyquery import PyQuery as pyq
#import codecs

reload(sys)
sys.setdefaultencoding('utf-8')

#Gets
headers =  header.getHeader("headerdata")
url = "https://www.hackthis.co.uk/levels/coding/1"
r = requests.get(url, headers = headers);

#pyq process
jq = pyq(r.text);
li = jq("textarea").text().split(', ');
li.sort();
payload = {'answer':', '.join(li)};

print payload
#Post
r = requests.post(url, data = payload, headers = headers);
#print r.text
