from rest_framework import serializers
from .models import CutoutQuery
from .validators import *


# TODO: 1. Format plot units with help text + label
#      2. Format Bands with multi select
#      3. Format Bands with help text + label 


class CutoutQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CutoutQuery
        fields = ('ra', 'dec', 'radius', 'bands', 'output_type')

    # Right Ascension
    ra = serializers.FloatField(
        label="RA",
        help_text="Right Ascension. Format is as: 10.2345",
    )

    # Declination
    dec = serializers.FloatField(
        help_text="Declination. Format is as: -0.2716",
    )

    # Radius
    radius = serializers.FloatField(
        label="Cutout radius (degrees)",
        help_text="Minimum value = 0.016666, maximum value = 5",
        min_value=0.016666,
        max_value=5.0,
    )
