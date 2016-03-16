from django.conf.urls import include, url, patterns 
from django.contrib import admin
admin.autodiscover()

'''
urlpatterns = [  
    url(r'^$', 'qa.views.test'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/\d+/$', 'qa.views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/.*$', 'qa.views.test'),
    url(r'^new/.*$', 'qa.views.test')
]

urlpatterns = patterns('qa.views',                                              
   url(r'^$', 'test'),                                                              
   url(r'^login/.*$', 'test', name='login'),                                    
   url(r'^signup/.*', 'test', name='signup'),                                   
   url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),                 
   url(r'^ask/.*', 'test', name='ask'),                                         
   url(r'^popular/.*', 'test', name='popular'),                                 
   url(r'^new/.*', 'test', name='new'),                                         
)
'''    
urlpatterns = patterns('',
    url(r'^$', 'test'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),                 
    url(r'^ask/.*', 'test', name='ask'),                                         
    url(r'^popular/.*', 'test', name='popular'),                                 
    url(r'^new/.*', 'test', name='new'),
    url(r'^admin/', admin.site.urls),
)