from django.conf.urls import url
from core.views import *

urlpatterns = [
    url(
        r'^$',
        core_index,
        name='index'
    ),

    url(
        r'^login/$',
        core_login,
        name='login'
    ),

    url(
        r'^logout/$',
        core_logout,
        name='logout'
    ),

    url(
        r'^register/$',
        core_register,
        name='register'
    ),
]