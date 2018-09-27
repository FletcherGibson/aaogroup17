from rest_framework import serializers
from .models import CutoutQuery

class CutoutQuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CutoutQuery
        fields = ('ra', 'dec', 'radius', 'bands', 'plot_units')