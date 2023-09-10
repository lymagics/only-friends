from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('friends/', include('friends.urls')),
    path('users/', include('users.urls')),
    path('notifications/', include('notifications.urls')),
]

app_name = 'api'
