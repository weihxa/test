from django.conf.urls import include, url
from django.contrib import admin
from dj_bbs import views as dj_bbs_views
from django.conf import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', dj_bbs_views.index),
    url(r'^index/', dj_bbs_views.index),
    url(r'^article/(\d*)', dj_bbs_views.article),
    url(r'^addfavor/', dj_bbs_views.addfavor),
    url(r'^blogtext/(\d*)', dj_bbs_views.blogtext),
    url(r'^about/$', dj_bbs_views.About),
]
