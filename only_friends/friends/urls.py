from django.urls import path

from friends.api import views

urlpatterns = [
    path('<int:pk>/add/', views.friend_add, name='add'),
    path('<int:pk>/remove/', views.friend_remove, name='remove'),
    path('<int:pk>/accept/', views.friend_accept, name='accept'),
    path('<int:pk>/refuse/', views.friend_refuse, name='refuse'),
    path('', views.friend_list, name='list'),
]

app_name = 'friends'
