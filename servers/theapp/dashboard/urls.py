from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
  url(r'^$',dashboard,name='dashboard'),
  url(r'^transactions.js/$',transactions,name='transactions'),
  url(r'^transaction/(?P<uuid>[^.]+).js/$',transaction,name='transaction'),
  url(r'^edit/(?P<uuid>.+)$',edit,name='edit'),
)
