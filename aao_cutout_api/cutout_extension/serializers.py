from rest_framework import serializers
from .models import CutoutQuery

#TODO: 1. Format plot units with help text + label
#      2. Format Bands with multi select
#      3. Format Bands with help text + label 

class CutoutQuerySerializer(serializers.HyperlinkedModelSerializer):

    #Radius
    radius = serializers.FloatField(
        min_value=0.016666,
        max_value=5.0,
        label="Cutout radius (degrees)",
        help_text="Minimum value = 0.016666, maximum value = 5"
    )

    # Right Ascension
    ra = serializers.CharField(
        label="RA",
        help_text="Right Ascension. Format is as: 10.2345",
    )

    # Declination
    dec = serializers.CharField(
        help_text= "Declination. Format is as: -0.2716",
    )

    class Meta: 
        model = CutoutQuery
        fields = ('ra', 'dec', 'radius', 'bands', 'plot_units')

    