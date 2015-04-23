#import header
#import requests
import sys
#import codecs

reload(sys)
sys.setdefaultencoding('utf-8')

#headers =  header.getHeader("headerdata")
#url = "https://www.hackthis.co.uk/levels/coding/1"
#payload = {}
#r = requests.get(url, headers = headers);
#f = codecs.open("out","w",'utf-8')
#f.write(r.text);
#f.close();

f = open('out')
data = f.read().strip('\n');
f.close();

print data.find("textarea")

#li = data.split(', ');
#li.sort();

