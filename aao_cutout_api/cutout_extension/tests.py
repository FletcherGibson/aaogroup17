import pytest
from cutout_extension.views import CutoutQueryView
from .models import CutoutQuery
from rest_framework.test import APIRequestFactory
from aao_cutout_api.settings.dev import *

pytestmark = pytest.mark.django_db


def test_account_is_configured():
    assert 'cutout_extension.apps.CutoutExtensionConfig' in INSTALLED_APPS


def test_bad_request_raises_exception():
    with pytest.raises(Exception) as e_info:
        c = CutoutQueryView.create(None, TestData.invalid_post)


def test_empty_request_raises_exception():
    with pytest.raises(Exception) as e_info:
        c = CutoutQueryView.create(None, empty_request)

class TestModel:

    def test_model(self):
        factory = APIRequestFactory()
        request = factory.post(TestData.valid_post, format='json')

class TestData:
    valid_post = {"ra": "10.2345",
            "dec": "-0.2716",
            "radius": 4.0,
            "bands": "mwagleam_dr1_072-080",
            "output_type": "fits",
            }

    invalid_post = {"ra": "10.2345",
            "dec": "-0.2716",
            "radius": 4.0,
            "bands": "mwagleam_dr1_072-080",
            "output_type": "fits",
            }
