# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.okooo.com/Lottery06/SoccerIndex.php?LotteryType=ToTo&LotteryNo=11037')

parser = BeautifulSoup(page)

#print parser.html.head.title

#print page.read().decode('GBK').encode('UTF-8')

#以下代码证明BeautifulSoup可以自动转码
#print parser.html.head.title
#matchList = parser.find('div', align='center')

print parser.html
'''
i = 1
for match in matchList:
    i = i + 1
    print i
    print match
'''
#print matchList
print 'finished'