import requests
import re
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer
from remote_imaging_micro_service.query_remote_image import query_gleam
from astropy.io.votable import parse


class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer

    def create(self, request):
        # field validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        return query_gleam(request)


def retrieve(self, request, pk=None):
    return Response(serialized_data, status=status.HTTP_200_OK)
