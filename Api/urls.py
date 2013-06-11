from django.conf.urls import patterns, url
from Api import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'work/color$', views.color, name='color'),
    url(r'work/color/ng$', views.colorNg, name='color'),
    url(r'work/j/color/$', views.colorj, name='color'),

)