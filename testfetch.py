# -*- coding: utf-8 -*-

from lxml import html

html = html.parse('http://www.okooo.com/Lottery06/SoccerIndex.php?LotteryType=ToTo&LotteryNo=11038')
link = html.getroot().xpath('//table[@id="TableBorder"]')
footballs = link[0].xpath('//tr[@class="WhiteBg BlueWord" or @class="ContentLight BlueWord"]')
items = footballs[0].findall("td")
print items
print 'finished'
