from django.conf.urls import patterns, url

from .views import PersonView

urlpatterns = [
    url(r'^(?P<remote_id>\d+)/$', PersonView.as_view(), name='person'),
]
