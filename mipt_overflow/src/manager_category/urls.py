from django.conf.urls import url
from manager_category.views import *

urlpatterns = [
    url(
        r'^$',
        category_index,
        name='index'
    ),

    url(
        r'^add/$',
        category_add,
        name='add'
    ),

    url(
        r'^list/$',
        category_list,
        name='list'
    ),

    url(
        r'^(?P<pk>\d+)/remove/$',
        category_remove,
        name='remove'
    ),

    url(
        r'^(?P<pk>\d+)/detail/$',
        category_detail,
        name='detail'
    ),

    url(
        r'^(?P<pk>\d+)/statistics/$',
        category_statistics,
        name='statistics'
    ),

    url(
        r'^list/statistics/$',
        category_list_statictics,
        name='list_statistics'
    ),
]