from django.conf.urls.defaults import patterns, include, url

#Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  #Allauth
  url(r'^accounts/', include('allauth.urls')),
  #Profile
  url(r'^accounts/profile/$','theapp.profiles.views.profile',name='account-profile'),

    # Examples:
    # url(r'^$', 'theapp.views.home', name='home'),
    # url(r'^theapp/', include('theapp.foo.urls')),

  #Admin
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
