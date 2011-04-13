# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.okooo.com/Lottery06/SoccerIndex.php?LotteryType=ToTo&LotteryNo=11037')

print '测试'
print page.read().decode('GBK').encode('UTF-8')