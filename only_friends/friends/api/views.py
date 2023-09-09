from django.http import Http404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth.authentication import JWTAuthentication
from core.decorators import output
from friends import services, selectors
from friends.errors import FriendError
from users.api.schemas import UserOut
from users.selectors import user_get


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def friend_add(request, pk: int):
    user = user_get(pk)
    if user is None:
        raise Http404
    try:
        services.friend_add(
            request.user, user,
        )
        return Response(status=200)
    except FriendError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def friend_remove(request, pk: int):
    user = user_get(pk)
    if user is None:
        raise Http404
    try:
        services.friend_remove(
            request.user, user,
        )
        return Response(status=200)
    except FriendError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def friend_accept(request, pk: int):
    user = user_get(pk)
    if user is None:
        raise Http404
    try:
        services.friend_offer_accept(
            user, request.user
        )
        return Response(status=200)
    except FriendError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def friend_refuse(request, pk: int):
    user = user_get(pk)
    if user is None:
        raise Http404
    try:
        services.friend_offer_refuse(
            user, request.user
        )
        return Response(status=200)
    except FriendError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)
    

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@output(UserOut, many=True)
def friend_list(request):
    return selectors.friend_list(request.user)
