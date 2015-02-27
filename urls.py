from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from mezzanine.core.views import direct_to_template

admin.autodiscover()

urlpatterns = i18n_patterns("",
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns('',
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    # url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),
    ("^", include("mezzanine.urls")),

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls")),
)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
