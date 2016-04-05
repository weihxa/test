#!/usr/bin/env python
#coding:utf-8
from django.utils.safestring import mark_safe
def html_fenye(page,allnum):
    ht=[]
    first_html="<a href='/article/%d'>首页</a>" %(1,)
    ht.append(first_html)
    if page==1:
        update_html="<a href='/article/%d'>上一页</a>" %(page,)
    else:
        update_html="<a href='/article/%d'>上一页</a>" %(page-1,)
    ht.append(update_html)
    if page <6:
        begin = 0
        if page+5 >allnum:
            end=allnum
        else:
            end=page+5
    else:
        begin =page-6
        if page+5 >allnum:
            end=allnum
        else:
            end=allnum+5
    #for i in range(zong):
    for i in range(begin,end):
        if page == i+1:
            a_html="<a class='selected' href='/article/%d'>%d</a>" %(i+1,i+1)
        else:
            a_html="<a href='/article/%d'>%d</a>" %(i+1,i+1)
        ht.append(a_html)
    end_html="<a href='/article/%d'>尾页</a>" %(allnum,)
    ht.append(end_html)
    if page==allnum:
        down_html="<a href='/article/%d'>下一页</a>" %(allnum,)
    else:
        down_html="<a href='/article/%d'>下一页</a>" %(page+1,)
    ht.append(down_html)
    #zongyeshu="<span>共%d页</span>" %(allnum,)
    #ht.append(zongyeshu)
    fen = mark_safe(''.join(ht))
    return fen