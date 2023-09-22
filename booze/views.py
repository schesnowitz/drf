from django.http import JsonResponse
from .models import Booze
from .serializers import BoozeSerializer

def booze_list(response):

  # get all booze
  booze = Booze.objects.all()
  # serialize the booze
  serializer = BoozeSerializer(booze, many=True)
  # return in JSON format
  # return JsonResponse(serializer.data, safe=False)
  # return as object -- can remove the safe=False param6
  return JsonResponse({'booze' : serializer.data})