from django.urls import path

from notifications.api import views

urlpatterns = [
    path('', views.notify_list, name='list'),
]

app_name = 'notifications'
