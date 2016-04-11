#!/usr/bin/env python
#coding:utf-8

import urllib
from bs4 import BeautifulSoup
import os
import Mysql
import Picture

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("https://linux.cn/news")
soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
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
    sql="INSERT INTO `dj_bbs_news`(title,summary,url,favor_count,reply_count,create_date,image_urls) VALUES('%s','%s','%s','0','0',NOW(),'news/%s.jpg');"%(Tltle,From,Url,x)
    Mysql.MysqlHelper().In_sql(sql)
    local = os.path.join('d:/','%s.jpg' % x)
    urllib.urlretrieve(Img,local)
    #处理图片
    Picture.timage("d:/%s.jpg" % x, 'd:/')
    x+=1

