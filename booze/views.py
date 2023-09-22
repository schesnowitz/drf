from django.http import JsonResponse
from .models import Booze
from .serializers import BoozeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

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