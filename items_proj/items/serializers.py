from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ['id', 'username'] 

class ItemSerializer(serializers.ModelSerializer):
    last_modified_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'last_modified_by']
