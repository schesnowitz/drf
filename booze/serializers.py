from rest_framework import serializers
from .models import Booze

class BoozeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booze
    fields = ['id', 'name', 'description']
