from django.db import models

BANDS_CHOICES = (
    ('mwagleam_dr1_072-080', 'MWA GLEAM DR1 072-080'),
    ('mwagleam_dr1_072-103', 'MWA GLEAM DR1 072-103 (stacked)'),
)

PLOTUNITS_CHOICES = (
    ('fits', 'FITS'),
    ('jpeg', 'JPEG'),
)

class CutoutQuery(models.Model):
    ra = models.CharField(
    help_text="Right Ascension. Format is as: 10.2345",
    max_length=30,
    )
    dec = models.CharField(
        help_text= "Declination. Format is as: -0.2716",
        max_length=30,
    )
    radius = models.FloatField(
                help_text="Minimum value = 0.016666, maximum value = 5")
    bands = models.CharField(max_length=len(BANDS_CHOICES), choices=BANDS_CHOICES, default=BANDS_CHOICES[0])
    plot_units = models.CharField(max_length=len(PLOTUNITS_CHOICES), choices=PLOTUNITS_CHOICES, default=PLOTUNITS_CHOICES[0])
