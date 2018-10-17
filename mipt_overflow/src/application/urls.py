from django.contrib import admin

from ranking.views import ranking
from tags.views import tags
from comments.views import comments

from django.conf import settings
from django.conf.urls import include, url

from jsonrpc import jsonrpc_site
from manager_user.views import upload_photo, upload_file, get_file
from manager_topic.views import topic_detail, topic_remove, topic_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('core.urls', namespace='core')),
    url(r'^user/', include('manager_user.urls', namespace='manager_user')),
    url(r'^topic/', include('manager_topic.urls', namespace='manager_topic')),
    url(r'^category/', include('manager_category.urls', namespace='manager_category')),

    url(r'^ranking/$', ranking),
    url(r'^tags/$', tags),
    url(r'^comments/$', comments),

    url(r'api/', jsonrpc_site.dispatch)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

