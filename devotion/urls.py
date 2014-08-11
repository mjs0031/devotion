from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from devotional.views import (devotionals, the_count,
                              specific_devotional,
                              create_devotional)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devotion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', devotionals),
    url(r'^count/$', the_count),
    url(r'^create/$', create_devotional.as_view()),
    url(r'^devotional/(\d+)/$', specific_devotional),
)
