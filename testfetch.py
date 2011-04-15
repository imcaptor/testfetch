# -*- coding: utf-8 -*-

from lxml import html
import string,sys

##使用方法：python testfetch.py 11037

def fetch_page(lottery_no):    
    page = html.parse('http://www.okooo.com/Lottery06/SoccerIndex.php?LotteryType=ToTo&LotteryNo=%s' % lottery_no)
    link = page.getroot().xpath('//table[@id="TableBorder"]')
    footballs = link[0].xpath('//tr[@class="WhiteBg BlueWord" or @class="ContentLight BlueWord"]')
    for football in footballs:
        items = football.findall("td")
        caiguo = items[5].find('strong').text;
        if not caiguo:
            caiguo = '-'
        line = items[0].text + '\t' + \
        items[1].find('a').text +'\t'+ \
        items[1].find('span').text.replace('\r\n', '').replace('\t', '') + '\t' + \
        items[2].text.strip() + '\t' + \
        items[2].find('span').text.replace('\r\n','').replace('\t', '') + '\t' + \
        items[3].find('a').text + '\t' + \
        items[3].find('span').text.replace('\r\n', '').replace('\t', '') + '\t' + \
        items[4].text + '\t' + \
        items[4].find('br').tail + '\t' + \
        caiguo + '\t' + \
        items[7].find('br').tail + '\t' + \
        items[8].find('br').tail + '\t' + \
        items[9].find('br').tail    
        print line    

def select_m_in_n(m, n):
    if m > n:
        return 0
    else:
        fenzi = 1
        fenmu = 1
        for i in range(m):
            fenzi = fenzi * (n-i)
            fenmu = fenmu * (m-i)            
        return fenzi/fenmu

if __name__ == '__main__':
    #fetch_page(sys.argv[1])
    print select_m_in_n(5, 14)
    print 'finished'
