from django.urls import path

from friends.api import views

urlpatterns = [
    path('<int:pk>/add/', views.friend_add, name='add'),
    path('<int:pk>/remove/', views.friend_remove, name='remove'),
]

app_name = 'friends'
