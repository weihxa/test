#!/usr/bin/env python
#coding:utf-8
from baike_sp import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()


if '__name__'=='__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm '
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
