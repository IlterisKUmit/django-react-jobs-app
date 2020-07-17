from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MissionsSerializer
from .models import Missions


# Create your views here....
class MissionsView(viewsets.ModelViewSet):
    serializer_class = MissionsSerializer
    queryset = Missions.objects.all()
