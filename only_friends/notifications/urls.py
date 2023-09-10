from django.urls import path

from notifications.api import views

urlpatterns = [
    path('count/', views.notify_count, name='count'),
    path('', views.notify_list, name='list'),
]

app_name = 'notifications'
