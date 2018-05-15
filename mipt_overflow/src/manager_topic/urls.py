from django.conf.urls import url
from manager_topic.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(
        r'^list/$',
        login_required(topic_list),
        name='list'
    ),

    url(
        r'^add/$',
        login_required(TopicAdd.as_view()),
        name='add'
    ),

    url(
        r'^(?P<pk>\d+)/edit/$',
        login_required(TopicEdit.as_view()),
        name='edit'
    ),

    url(
        r'^(?P<pk>\d+)/detail/$',
        login_required(topic_detail),
        name='detail'
    ),

    url(
        r'^(?P<pk>\d+)/remove/$',
        login_required(topic_remove),
        name='remove'
    ),

]