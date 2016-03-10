from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^list2/', views.post_list2, name='post_list2'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]