from django.conf.urls.defaults import patterns, include, url

#Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  #Dashboard
  url(r'^$','theapp.dashboard.views.dashboard',name='dashboard'),

  #Profile
  url(r'^accounts/profile/$','theapp.profiles.views.profile',name='account-profile'),

  #Allauth
  url(r'^accounts/', include('allauth.urls')),

  #Admin
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
