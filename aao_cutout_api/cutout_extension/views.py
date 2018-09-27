import requests
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from xml.etree import ElementTree
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer

class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer

    def create(self, request): 
        post_data = request.data
        position = "{},{}".format(post_data['ra'],post_data['dec'])
        payload = {
            # 'POS':'0.4298047815961236,-0.4903328000552869',
            'POS' : position,
            'SIZE': post_data['radius'],
            'BAND': post_data['bands'],
            'FORMAT' : post_data['plot_units']
        }
        r = requests.get(
        "http://gleam-vo.icrar.org/gleam_postage/q/siap.xml?", params=payload)
        #return Response(r.text)
        return Response(r.url)

    def retrieve(self, request, pk=None):
        # your code

        return Response(serialized_data, status=status.HTTP_200_OK)