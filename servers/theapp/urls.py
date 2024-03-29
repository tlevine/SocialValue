from django.conf.urls.defaults import patterns, include, url

#Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  #Dashboard
  url(r'^', include('dashboard.urls')),

  #Identity and API for checking identity
  url(r'^accounts/profile/$','theapp.profiles.views.profile',name='account-profile'),
  url(r'^who/',include('keychain.urls')),

  #Allauth
  url(r'^accounts/', include('allauth.urls')),


  #Admin
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
