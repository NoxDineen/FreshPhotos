from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gallery/([\w-]+)/$', 'freshphotos.photos.views.gallery'),
    url(r'^gallery/([\w-]+)/(carousel)/$', 'freshphotos.photos.views.gallery'),
    url(r'^photo/([\w-]+)/$', 'freshphotos.photos.views.photo'),
    # Examples:
    # url(r'^$', 'freshphotos.views.home', name='home'),
    # url(r'^freshphotos/', include('freshphotos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)