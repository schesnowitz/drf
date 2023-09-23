from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booze

class BoozeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booze
    fields = ['id', 'name', 'description']




class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']