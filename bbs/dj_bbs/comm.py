#!/usr/bin/env python
#coding:utf-8
def zhuanint(pag,default):
    try:
        pag = int(pag)
    except Exception,e:
        pag = 1
    return pag