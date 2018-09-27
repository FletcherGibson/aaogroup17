from django.shortcuts import render
from rest_framework import viewsets
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer

class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer