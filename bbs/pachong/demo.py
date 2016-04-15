#!/usr/bin/env python
#coding:utf-8

import urllib2
import urllib
from bs4 import BeautifulSoup
import os
import Mysql
import Picture

def getHtml(url):
    #page = urllib2.urlopen(url)
    #html = page.read()
    # return html
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5"}
    req = urllib2.Request(url=url,headers=headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    #socket.close()
    return html

html = getHtml("https://linux.cn/news")
#print html
soup = BeautifulSoup(str(html),'html.parser',from_encoding='utf-8')
#print soup
From = soup.title.get_text()
Div = soup.find_all('div',class_='carousel-caption')
#清空原来数据
sql="TRUNCATE `dj_bbs_news;"
Mysql.MysqlHelper().In_sql(sql)

x = 1
for line in Div:
    soup2 = BeautifulSoup(str(line),'html.parser',from_encoding='utf-8')
    Url = soup2.find('a')['href']
    html2 = getHtml(soup2.find('a')['href'])
    Tltle = BeautifulSoup(html2,'html.parser',from_encoding='utf-8').find('h1',class_='ph').get_text()
    Img = soup.find('img',alt='%s' % Tltle.strip())['src']
    #print Img
    try:
        sql='''INSERT INTO `dj_bbs_news`(title,summary,url,favor_count,reply_count,create_date,image_urls) VALUES("%s",'%s','%s','0','0',NOW(),'news/%s.jpg');''' %(Tltle,From,Url,x)
        #print sql
        Mysql.MysqlHelper().In_sql(sql)
    except Exception,e:
        print e
    local = os.path.join('D:/test/bbs/static/news/','%s.jpg' % x)
    urllib.urlretrieve(Img,local)
    #处理图片
    Picture.timage("D:/test/bbs/static/news/%s.jpg" % x, 'D:/test/bbs/static/news/')
    print '已处理完%s.jpg'% x
    x+=1

