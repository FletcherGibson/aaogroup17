import requests
import re
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer
from remote_imaging_micro_service.query_remote_image import parse_votable
from astropy.io.votable import parse


class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer

    # TODO: 1. Assign freq band to website in order to
    #         be able to query based on frequency.
    #      2. Make sure that POST also saves to DB for

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        site = "http://gleam-vo.icrar.org/gleam_postage/q/siap.xml?"
        post_data = request.data
        gleam_payload = ['POS', 'SIZE', 'FREQ', 'FORMAT']
        # GLEAM

        return parse_votable(site, gleam_payload, post_data)

def retrieve(self, request, pk=None):
    return Response(serialized_data, status=status.HTTP_200_OK)
