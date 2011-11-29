from django.conf.urls.defaults import patterns, include, url
from views import dashboard,transactions

urlpatterns = patterns('',
  url(r'^$',dashboard,name='dashboard'),
  url(r'^transactions.js/$',transactions,name='transactions'),
)
