from cutout_extension.views import *
from aao_cutout_api.settings.dev import *

def test_account_is_configured():
    assert 'cutout_extension.apps.CutoutExtensionConfig' in INSTALLED_APPS