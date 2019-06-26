from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^send_dummy/', views.send_dummy, name='send_dummy'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
]