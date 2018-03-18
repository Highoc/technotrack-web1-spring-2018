from django.conf.urls import url
from manager_user.views import *

urlpatterns = [
    url(
        r'^home/$',
        user_index,
        name='index'
    ),

    url(
        r'^info/$',
        user_info,
        name='info'
    )
]