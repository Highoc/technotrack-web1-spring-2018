from django.conf.urls import url
from manager_topic.views import *

urlpatterns = [
    url(
        r'^list/$',
        topic_list,
        name='list'
    ),

    url(
        r'^add/$',
        topic_add,
        name='add'
    ),

    url(
        r'^(?P<pk>\d+)/detail/$',
        topic_detail,
        name='detail'
    ),

    url(
        r'^(?P<pk>\d+)/remove/$',
        topic_remove,
        name='remove'
    ),

    url(
        r'^(?P<pk>\d+)/statistics/$',
        topic_statistics,
        name='statistics'
    )
]