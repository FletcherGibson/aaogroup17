import re
from rest_framework.response import Response
import requests
from astropy.io.votable import parse


def query_gleam(request):
    """
    Queries the site with a specified payload.
    :param request: The request to be sent
    :return: A call to parse_votable
    """
    site = "http://gleam-vo.icrar.org/gleam_postage/q/siap.xml?"
    data = request.data
    gleam_payload = ['POS', 'SIZE', 'FREQ', 'FORMAT']

    position = [data['ra'], data['dec']]
    payload = {
        gleam_payload[0]: ','.join(position),
        gleam_payload[1]: data['radius'],
        gleam_payload[2]: re.sub(r'^mwagleam_dr1_', '', data['bands']),
        gleam_payload[3]: data['output_type']
    }

    return parse_votable(site, payload, data)


def parse_votable(site, payload, data):
    """

    :param site: The site to query
    :param payload: The payload for a GET request
    :param data: the data to be used in the payload
    :return: A response from the
    """
    r = requests.get(site, params=query_gleam(payload, data))
    create_voteable_local(r)
    response = extract_files_from_votable()

    return response


def create_voteable_local(r):
    """
    Creates a readable votable.xml file
    :param r: a request from the queried site
    :return:
    """
    with open('votable.xml', 'w') as f:
        f.write(r.text)
        f.close()

    votable = parse("votable.xml")
    votable.to_xml("votable.xml")

    return votable


def extract_files_from_votable():
    """
    Extracts only the required data from the VOTable.XML file
    :return: The extracted results from the VOTable.XML file
    """
    f2 = open('votable.xml', 'r+')
    lines = f2.readlines()
    for line in lines:
        if line[10:14] == "http":  # find url
            result = line[10:len(line) - 6]  # remove tags
            fits = result.replace("&amp;", "&")  # format url parameters
            png = fits.replace("fits_format=1", "fits_format=0")
            results = [fits, png]
            response = Response(results)
    f2.close()

    return response
