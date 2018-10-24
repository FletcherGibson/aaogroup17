import requests
import re
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import CutoutQuery
from .serializers import CutoutQuerySerializer
from astropy.io.votable import parse


class CutoutQueryView(viewsets.ModelViewSet):
    queryset = CutoutQuery.objects.all()
    serializer_class = CutoutQuerySerializer

    # TODO: 1. Assign freq band to website in order to
    #         be able to query based on frequency.
    #      2. Make sure that POST also saves to DB for
    #

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        site = "http://gleam-vo.icrar.org/gleam_postage/q/siap.xml?"
        post_data = request.data
        gleam_payload = ['POS', 'SIZE', 'FREQ', 'FORMAT']

        # GLEAM
        r = requests.get(site, params=self.query_gleam(gleam_payload, post_data))
        response = Response(r.url)

        with open('votable.xml', 'w') as f:
            f.write(r.text)
            f.close()

        votable = parse("votable.xml")
        votable.to_xml("votable.xml")

        f2 = open('votable.xml', 'r+')
        lines = f2.readlines()
        for line in lines:
            if line[10:14] == "http": #find url
                result = line[10:len(line) - 6] #remove tags
                url = result.replace("&amp;", "&") #format url parameters
                response = Response(url)
        f2.close()
        return response

    @staticmethod
    def query_gleam(query_list, data):

        position = [data['ra'], data['dec']]
        payload = {
            query_list[0]: ','.join(position),
            query_list[1]: data['radius'],
            query_list[2]: re.sub(r'^mwagleam_dr1_', '', data['bands']),
            query_list[3]: data['output_type']
        }

        return payload


    def retrieve(self, request, pk=None):
        return Response(serialized_data, status=status.HTTP_200_OK)
