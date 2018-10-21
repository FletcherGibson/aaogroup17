import pytest
from cutout_extension.views import CutoutQueryView
from aao_cutout_api.settings.dev import *


def test_account_is_configured():
    assert 'cutout_extension.apps.CutoutExtensionConfig' in INSTALLED_APPS


def test_bad_request_raises_exception():
    bad_req = bad_request()
    with pytest.raises(Exception) as e_info:
        c = CutoutQueryView.create(None, bad_req)


def test_empty_request_raises_exception():
    with pytest.raises(Exception) as e_info:
        c = CutoutQueryView.create(None, empty_request)


def test_create_request():
    req = request()
    cq = CutoutQueryView()
    r = CutoutQueryView.create(cq, req)
    assert r != None


class request:
    data = {"ra": "10.2345",
            "dec": "-0.2716",
            "radius": 4.0,
            "bands": "mwagleam_dr1_072-080",
            "output_type": "fits",
            }


class bad_request:
    data = {"This is an example of bad request data"}
