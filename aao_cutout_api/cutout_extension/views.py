import requests
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer

class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer

    #TODO: 1. Assumg freq band to website in order to
    #         be able to query based on frequency.
    #      2. Make sure that POST also saves to DB for
    #         
    def create(self, request): 
        post_data = request.data
        position = "{},{}".format(post_data['ra'],post_data['dec'])
        payload = {
            # 'POS':'0.4298047815961236,-0.4903328000552869',
            'POS' : position,
            'SIZE': post_data['radius'],
            #FREQ=072-080 VALID
            #FREQ=mwagleam_dr1_072-080 INVALID 
            'FREQ': post_data['bands'],
            'FORMAT' : post_data['output_type']
        }
        r = requests.get("http://gleam-vo.icrar.org/gleam_postage/q/siap.xml?", params=payload)
        return Response(r.url)

    def retrieve(self, request, pk=None):
        # your code

        return Response(serialized_data, status=status.HTTP_200_OK)