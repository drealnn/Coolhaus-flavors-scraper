from lxml import html
import requests
import json
import urllib2

page = requests.get('http://eatcoolhaus.com/menu')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@class="chlistitem chli_darkgray"]/@data-info')
strings = []
handles = []
titles = []
descriptions = []

flavorJson = []

for buyer in buyers:
    jsonstring = json.loads(buyer)
    #flavorJson.append(buyer)
    if len(jsonstring['handle']) > 0:
        strings.append(jsonstring['menutype'] + '/'+jsonstring['handle']) 
    titles.append(jsonstring['label'])
    handles.append(jsonstring['handle'])
    descriptions.append(jsonstring['description'])
'''

for title in titles:
    print titl 
'''

'''
print strings
extensions = ['jpg']
for imagename in strings:
    for extension in extensions:
	url =  "http://www.eatcoolhaus.com/images/menu/" + imagename + "." + extension
	print url + "\n"
        #urllib.urlretrieve(url, url.split('/')[-1])
	
	req = urllib2.Request(url)

	# add user-agent header to our request, a simple string identifying the browser
	# in this case the user-agent is for Firefox 24, the current ESR
	req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0")
	try:
	    r = urllib2.urlopen(req)
	    data = r.read()
	    with open(url.split('/')[-1], "w") as f:
	        f.write(data)
	except:
	    pass
'''
print flavorJson

