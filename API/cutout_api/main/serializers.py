from rest_framework import serializers
from .models import CutoutQuery


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
        help_text="Miniamum value = 0.016666, maximum value = 5",
        min_value=0.016666,
        max_value=5.0,
    )
