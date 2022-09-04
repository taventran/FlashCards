from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CardSerializer, SetSerializer
from .models import Card, Set


def test(request):
    return HttpResponse('<h1>TESTING</h1>')

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, ) 
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, ) 

    @action(detail=True, methods=["POST"])
    def makeCard(self, request):
        if 'set' and 'definition' and 'term' in request.data:
            set = request.data['set']
            serializer = CardSerializer
            definition = request.data['definition']
            term = request.data['term']

            card = Card.objects.create(set=set, definition=definition, term=term)
            response = {'message': 'New card created', 'result':serializer.data}
            return Response(response, status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide a set name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, ) 

    @action(detail=True, methods=["POST"])
    def setName(self, request):
        if 'setName' in request.data:
            setName = request.data['setName']
            user = request.user
            serializer = SetSerializer
            set = Set.objects.create(user=user, setName=setName)
            response = {'message': 'New set created', 'result': serializer.data}
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide a set name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
