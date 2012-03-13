from django.conf.urls.defaults import patterns, include, url
from givalittle.views import *
from django.contrib import admin
from django.views.static import *
from django.conf import settings
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'givalittle.views.home', name='home'),
    # url(r'^givalittle/', include('givalittle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', home),
    url(r'give/', give),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^test/$', test),
    url(r'^get/$', get),
)
