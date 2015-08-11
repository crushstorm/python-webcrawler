from bs4 import BeautifulSoup
import urllib2
import re

import sys

list = []
url = sys.argv[1]
#url = 'http://www.spotify.com'

def PrintMetaDescription(soup):
  	md = ''
  	l = soup.findAll("meta", attrs={"name":"description"})
  	if l != []:
  	#else:
   		list.append(l[0]['content'].encode('utf-8'))
  	
def PrintMetaKeywords(soup):
	mk = ''
	l = soup.findAll("meta", attrs={"name":"keywords"})
  	if l != []:
   	#else:
   		list.append(l[0]['content'].encode('utf-8'))
  	
def PrintMetaTitle(soup):
	mk = ''
	l = soup.findAll("meta", attrs={"name":"title"})
  	if l != []:
   	#else:
   		list.append(l[0]['content'].encode('utf-8'))
  	

def geth4(soup):
	l = soup.findAll('h4')
	denylist = ['Image Unavailable','MUST WATCH']
	for k in l:
		if str(k.get_text()) not in (denylist[:1]+denylist[:2]):
			list.append(str(k.get_text()))
	#list.append(l)
	
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
PrintMetaDescription(soup)
PrintMetaKeywords(soup)
geth4(soup)
PrintMetaTitle(soup)
final = set()
for i in list: 
	temp =  re.findall(r'(?:\d[,]|[^,])*(?:[,]|$)',i)
	for j in temp:
		if j:
			j = j.rstrip(',')
			final.add(j.lstrip())
print "\nRelevant keywords : "
for i in final:
	print i
#print final
