from django.conf.urls import patterns, url
from Api import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'work/color$', views.color, name='color'),
)