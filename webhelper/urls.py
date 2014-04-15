from django.conf.urls import patterns, url
from webhelper.views import home


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^reusable/', include('reusable.foo.urls')),
                       url(r'^$', home.as_view(), name='webhelper-home'),
                       )
