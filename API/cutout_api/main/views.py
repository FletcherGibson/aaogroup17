from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from remote_imaging_micro_service.models import CutoutQuery
from remote_imaging_micro_service.serializers import CutoutQuerySerializer


class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer
