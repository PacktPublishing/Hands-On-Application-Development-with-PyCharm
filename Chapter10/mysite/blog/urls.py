from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # list view
    url(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'
    ),  # detail view
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),  # share view
]
