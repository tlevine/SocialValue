from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
  url(r'^$',dashboard,name='dashboard'),
  url(r'^transactions.js/$',transactions,name='transactions'),
  url(r'^transaction/(?P<uuid>[^.]+).js/$',transaction,name='transaction'),
  url(r'^new/(?P<uuid>.*)$',edit,name='new'),
  url(r'^edit/(?P<uuid>.*)$',edit,name='edit'),
  url(r'^sign/(?P<uuid>.*)$',sign,name='sign'),
)
