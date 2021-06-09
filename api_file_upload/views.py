from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()