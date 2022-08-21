from rest_framework import serializers
from django.conf import settings
from .models import Set, Card
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required':True}}

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('term', 'definition', 'set')

class SetSerializer(serializers.ModelSerializer):

    cards = CardSerializer(many=True)

    class Meta:
        model = Set
        fields = ('id', 'setName', 'user', 'cards')

