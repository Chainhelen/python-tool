import header
import requests
import sys
from pyquery import PyQuery as pyq
#import codecs

reload(sys)
sys.setdefaultencoding('utf-8')

#Gets
headers =  header.getHeader("headerdata")
url = "https://www.hackthis.co.uk/levels/coding/2"
r = requests.get(url, headers = headers);

def getChar(string):
    ll = string.split(',');
    ll = map(int, ll);
    res = '';
    for i in ll:
        res += chr(158 - i)
    return res


#pyq process
jq = pyq(r.text);
li = jq("textarea").text().split(', ,');
res = [];

for i in li:
    res.append(getChar(i));

#print ' '.join(res)
#payload = {'answer':', '.join(li)};
payload = {'answer':' '.join(res)};

print payload
#Post
r = requests.post(url, data = payload, headers = headers);
#print r.text
