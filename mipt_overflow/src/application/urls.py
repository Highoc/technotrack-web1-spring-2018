"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from manager_user.views import index, user_home
from manager_topic.views import topic_detail, topic_list, topic_add
from manager_category.views import category_list, category_detail
from ranking.views import ranking


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^topic/(\d+)/$', topic_detail),
    url(r'^topic/list/$', topic_list),
    url(r'^topic/add/$', topic_add),
    url(r'^home/$', user_home),
    url(r'^ranking/$', ranking),
    url(r'^category/list/$', category_list),
    url(r'^category/(?P<pk>\d+)/$', category_detail),
]
