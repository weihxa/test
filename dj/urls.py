from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views
from session import views as session_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'dj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', learn_views.home, name='home'),
    url(r'^time/(\d{1,2})/$', learn_views.hours_ahead, name='hours_ahead'),
    url(r'^add/(?P<name>\d*)/$',learn_views.Add),
    url(r'^del/(?P<id>\d*)/$',learn_views.DEL),
    url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$',learn_views.UPDATE),
    url(r'^asset/$',learn_views.AssetList),
    url(r'^login/$',learn_views.Login),
    url(r'^regiter/$',learn_views.register),
    url(r'^ajax/$',learn_views.ajax),
    url(r'^fenye/(\d*)',learn_views.fenye),
    url(r'^sess/login/',session_views.login),
    url(r'^sess/index/',session_views.index),
    url(r'^sess/logout/',session_views.logout),
]
