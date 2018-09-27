from rest_framework import serializers
from .models import CutoutQuery

class CutoutQuerySerializer(serializers.HyperlinkedModelSerializer):

    #Radius
    radius = serializers.FloatField(
        min_value=0.016666,
        max_value=5.0,
        label="Cutout radius (degrees)",
        help_text="Minimum value = 0.016666, maximum value = 5"
    )

    #Format
    plot_units = serializers.CharField(
        label="Format",
        required=True,
    )

    # Right Ascension
    ra = serializers.CharField(
        label="RA",
        help_text="Right Ascension. Format is as: 10.2345",
    )

    # Declination
    dec = serializers.CharField(
         help_text= "Declination. Format is as: -0.2716"
    )

    #TODO: Fill in help text
    #      Many to Many relation/selection
    #Frequency Bands
    bands = serializers.CharField(
        help_text="Some useful info about this parameter",
    )

    class Meta: 
        model = CutoutQuery
        fields = ('ra', 'dec', 'radius', 'bands', 'plot_units')