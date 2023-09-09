from django.urls import path

from friends.api import views

urlpatterns = [
    path('<int:pk>/add/', views.friend_add, name='add'),
]

app_name = 'friends'
