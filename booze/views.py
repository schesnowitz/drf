from django.http import JsonResponse
from .models import Booze
from .serializers import BoozeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(http_method_names=['GET', 'POST'])
def booze_list(request):
  if request.method == "GET":
    # get all booze
    booze = Booze.objects.all()
    # serialize the booze
    serializer = BoozeSerializer(booze, many=True)
    # return in JSON format
    # return JsonResponse(serializer.data, safe=False)
    # return as object -- can remove the safe=False param6
    return JsonResponse({'booze' : serializer.data})
  
  if request.method == "POST":
    serializer = BoozeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)