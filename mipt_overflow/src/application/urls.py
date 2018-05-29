from django.conf.urls import url, include
from django.contrib import admin

from ranking.views import ranking
from tags.views import tags
from comments.views import comments

from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('core.urls', namespace='core')),
    url(r'^user/', include('manager_user.urls', namespace='manager_user')),
    url(r'^topic/', include('manager_topic.urls', namespace='manager_topic')),
    url(r'^category/', include('manager_category.urls', namespace='manager_category')),

    url(r'^ranking/$', ranking),
    url(r'^tags/$', tags),
    url(r'^comments/$', comments),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
