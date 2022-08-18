from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CardSerializer, SetSerializer
from .models import Card, Set

# Create your views here.
def test(request):
    return HttpResponse('<h1>TESTING</h1>')

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer