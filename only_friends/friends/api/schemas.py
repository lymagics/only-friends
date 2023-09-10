from rest_framework import serializers

from notifications.models import Notification


class NotificationOut(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'name', 'payload')
