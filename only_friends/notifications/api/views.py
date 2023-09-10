from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth.authentication import JWTAuthentication
from core.decorators import output
from notifications import selectors, services
from notifications.api.schemas import NotificationOut


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@output(NotificationOut, many=True)
def notify_list(request):
    status = request.query_params.get('status', 'all')
    notifications = selectors.notify_list(request.user, status=status)
    services.notify_mark_seen(notifications)
    return notifications


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def notify_count(request):
    count = selectors.notify_count(request.user)
    return Response(count, status=200)
