from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserProfileViewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    fav_color = request.GET["fav_color"]

    message = "I don't have anything to say about your fav color"

    if fav_color == "blue":
        message = 'sky is blue'
    elif fav_color == "yellow":
        message = 'sun is yellow'

    return HttpResponse(message)

@api_view(['POST'])
def create_user(request):

    serializer = UserCreateSerializer(data=request.data)

    response_data = {
        "errors": None,
        "data": None
    }

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        response_data["data"] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data['errors'] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

def user_list(request):

    print('Request user object -> ', request.user)

    users = UserProfile.objects.all()

    serialized_data = UserProfileViewSerializer(instance=users, many=True)

    return Response(serialized_data.data, status=status.HTTP_200_OK)
