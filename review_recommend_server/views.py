from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, status, permissions
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

import requests

from .models import Movies, User
from .serializers import MovieSerializer, UserSerializer
from django.conf import settings


# Create your views here.
def home(request):
    return HttpResponse("Home")


#
class MoviesViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Movies.objects.all()[:6]
    serializer_class = MovieSerializer

    @api_view(['GET'])
    def get_movies(self, request):
        return Response(MovieSerializer.data)


#
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user).data)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)

