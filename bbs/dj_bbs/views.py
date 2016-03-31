from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from dj_bbs import models
import json
# Create your views here.

def index(request):
    blog_list = models.BlogsPost.objects.filter(favor_count__gt=10)[0:10]
    return render_to_response('index.html',{'blog_list':blog_list})

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
def article(request):
    blog_list = models.BlogsPost.objects.all()
    return render_to_response('article.html',{'blog_list':blog_list})

def blogtext(request,page):
    blog_list = models.BlogsPost.objects.get(id=page)
    return render_to_response('blogtext.html',{'blog_list':blog_list})