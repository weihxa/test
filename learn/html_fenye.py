#!/usr/bin/env python
#coding:utf-8
from django.utils.safestring import mark_safe
def html_fenye(page,zong):
    ht=[]
    first_html="<a href='/fenye/%d'>首页</a>" %(1,)
    ht.append(first_html)
    if page==1:
        update_html="<a href='/fenye/%d'>上一页</a>" %(page,)
    else:
        update_html="<a href='/fenye/%d'>上一页</a>" %(page-1,)
    ht.append(update_html)
    if page <6:
        begin = 0
        if page+5 >zong:
            end=zong
        else:
            end=page+5
    else:
        begin =page-6
        if page+5 >zong:
            end=zong
        else:
            end=page+5
    #for i in range(zong):
    for i in range(begin,end):
        if page == i+1:
            a_html="<a class='selected' href='/fenye/%d'>%d</a>" %(i+1,i+1)
        else:
            a_html="<a href='/fenye/%d'>%d</a>" %(i+1,i+1)
        ht.append(a_html)
    end_html="<a href='/fenye/%d'>尾页</a>" %(zong,)
    ht.append(end_html)
    if page==zong:
        down_html="<a href='/fenye/%d'>下一页</a>" %(zong,)
    else:
        down_html="<a href='/fenye/%d'>下一页</a>" %(page+1,)
    ht.append(down_html)
    fen = mark_safe(''.join(ht))
    return fen