from lxml import html
import requests
import json
import urllib

page = requests.get('http://eatcoolhaus.com/menu')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@class="chlistitem chli_darkgray"]/@data-info')
strings = []
for buyer in buyers:
    jsonstring = json.loads(buyer)
    if len(jsonstring['handle']) > 0:
        strings.append(jsonstring['menutype'] + '/'+jsonstring['handle']) 
    print jsonstring['handle']

print strings
extensions = ['jpg']
for imagename in strings:
    for extension in extensions:
	url =  "http://www.eatcoolhaus.com/images/menu/" + imagename + "." + extension
	print "http://www.eatcoolhaus.com/images/menu/" + imagename + "." + extension + "\n"
        urllib.urlretrieve(url, url.split('/')[-1])
