#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.template.context import RequestContext
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'whx' and pwd == '123':
            request.session['is_login']={'user':user}
            return redirect('/sess/index')
        else:
           return render_to_response('session/login.html',{'res':'密码不对'},context_instance=RequestContext(request))
    return render_to_response('session/login.html',context_instance=RequestContext(request))


def index(request):
    user_dict=request.session.get('is_login',None)
    if user_dict:
        return render_to_response('session/index.html',{'user':user_dict['user']})
    else:
        return redirect('/sess/login')
    #return render_to_response('session/index.html')

def logout(request):
    #del request.session['is_login']
    user_dict=request.session.get('is_login',None)
    if user_dict:
        del request.session['is_login']
        return render_to_response('session/login.html',context_instance=RequestContext(request))
    else:
        return render_to_response('session/login.html',context_instance=RequestContext(request))