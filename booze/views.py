from django.http import JsonResponse
from .models import Booze
from .serializers import BoozeSerializer, UserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(http_method_names=['GET', 'POST'])

def booze_list(request, format=None):
  if request.method == "GET":
    # get all booze
    booze = Booze.objects.all()
    # serialize the booze
    serializer = BoozeSerializer(booze, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  if request.method == "POST":
    serializer = BoozeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def booze_detail(request, pk, format=None):   
  try: 
    booze = Booze.objects.get(pk=pk)
  except Booze.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = BoozeSerializer(booze)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  if request.method == "PUT":
    serializer = BoozeSerializer(booze, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == "DELETE":
    booze.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
  


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")