from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from dj_bbs import models
import json
import comm
from django.utils.safestring import mark_safe
import html_fenye
# Create your views here.

def index(request):
    blog_list = models.BlogsPost.objects.filter(favor_count__gt=10)[0:10]
    new_list = models.News.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list,'new_list':new_list})

def addfavor(request):
    ret = {'status':0,'data':'','message':''}
    try:
        id = request.POST.get('nid')
        blogObj = models.BlogsPost.objects.get(id=id)
        temp = blogObj.favor_count + 1
        blogObj.favor_count = temp
        blogObj.save()
        ret['status'] = 1
        ret['data'] = temp
    except Exception,e:
        ret['message'] = e.message
    return HttpResponse(json.dumps(ret))
def article(request,page):
    #blog_list = models.BlogsPost.objects.all()
    #tianshu=comm.zhanint(request.COOKIES.get('pager_num',10),10)
    disnum = 5
    page=comm.zhuanint(page,1)
    #result = models.BlogsPost.objects.all()[(int(page)-1)*tianshu:int(page)*tianshu]
    blog_list = models.BlogsPost.objects.all()[(int(page)-1)*disnum:int(page)*disnum]
    coun = models.BlogsPost.objects.all().count()
    temp = divmod(coun,disnum)
    if temp[1]==0:
        allnum = temp[0]
    else:
        allnum=temp[0]+1
    if page >allnum:
        page=allnum
        Paging=html_fenye.html_fenye(page,allnum)
    else:
        Paging=html_fenye.html_fenye(page,allnum)
    return render_to_response('article.html',{'blog_list':blog_list,'Paging':Paging})

def blogtext(request,page):
    blog_list = models.BlogsPost.objects.get(id=page)
    return render_to_response('blogtext.html',{'blog_list':blog_list})

def About(request):
    return render_to_response('about.html')