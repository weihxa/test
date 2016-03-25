#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse ,Http404
import datetime
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from learn.models import Asset,Host
from learn.forms import registerform
import json
import comm
from django.utils.safestring import mark_safe
import html_fenye
# Create your views here.
'''
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) +int(b)
    return HttpResponse(str(c))
'''

def home(request):
    return render(request,'home.html')

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #t = get_template('current_datetime.xhtml')
    #html = t.render(Context({'current_date':dt}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.xhtml',{'current_date':dt})

def Add(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse('OK')

def DEL(request,id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('OK')

def UPDATE(request,id,hostname):
    obj=Asset.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
    return HttpResponse('OK')

def AssetList(request):
    asset_list=Asset.objects.all()
    return render_to_response('asset.html',{'data':asset_list,'user':'滚粗'})
def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        asset_list=Asset.objects.all()
        return render_to_response('asset.html',{'data':asset_list,'user':'滚粗'})
    else:
        return render_to_response('login.html')

def register(request):

    registerForm=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print data
            return Login(request)
            #return render_to_response('register.html',{'from':registerForm})

        else:
            print form.errors
            return render_to_response('register.html',{'from':registerForm})
    else:
        return render_to_response('register.html',{'from':registerForm})

    '''
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        asset_list=Asset.objects.all()
        return render_to_response('asset.html',{'data':asset_list,'user':'滚粗'})
    else:
        return render_to_response('login.html')
    '''

def ajax(request):
    if request.method == 'POST':
        print request.POST
        data = {'status':0,'msg':'请求成功','data':[11,22,33]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('ajax.html')


def fenye(request,page):
    tianshu = 20
    page=comm.zhanint(page,1)
    result = Host.objects.all()[(int(page)-1)*tianshu:int(page)*tianshu]
    coun = Host.objects.all().count()
    temp = divmod(coun,tianshu)
    if temp[1]==0:
        zong = temp[0]
        print zong
    else:
        zong=temp[0]+1
    if page >zong:
        page=zong
        fen=html_fenye.html_fenye(page,zong)
    else:
        fen=html_fenye.html_fenye(page,zong)
    return render_to_response('fenye.html',{'data':result,'cont':coun,'yema':page,'zong':zong,'ht':fen})