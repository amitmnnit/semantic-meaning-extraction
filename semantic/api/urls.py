from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls import include

urlpatterns = patterns('',
    #Auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^trend/$', views.TweetTrend.as_view()),

    )

urlpatterns = format_suffix_patterns(urlpatterns)