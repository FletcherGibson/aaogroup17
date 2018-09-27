from django.db import models

BANDS_CHOICES = (
    ('mwagleam_dr1_072-080', 'MWA GLEAM DR1 072-080'),
    ('mwagleam_dr1_072-103', 'MWA GLEAM DR1 072-103 (stacked)'),
    ('mwagleam_dr1_072-080', 'MWA GLEAM DR1 072-080'),
    ('mwagleam_dr1_072-103', 'MWA GLEAM DR1 072-103 (stacked)'),
    ('mwagleam_dr1_080-088', 'MWA GLEAM DR1 080-088'),
    ('mwagleam_dr1_088-095', 'MWA GLEAM DR1 088-095'),
    ('mwagleam_dr1_095-103', 'MWA GLEAM DR1 095-103'),
    ('mwagleam_dr1_103-111', 'MWA GLEAM DR1 103-111'),
    ('mwagleam_dr1_103-134', 'MWA GLEAM DR1 103-134 (stacked)'),
    ('mwagleam_dr1_111-118', 'MWA GLEAM DR1 111-118'),
    ('mwagleam_dr1_118-126', 'MWA GLEAM DR1 118-126'),
    ('mwagleam_dr1_126-134', 'MWA GLEAM DR1 126-134'),
    ('mwagleam_dr1_139-147', 'MWA GLEAM DR1 139-147'),
    ('mwagleam_dr1_139-170', 'MWA GLEAM DR1 139-170 (stacked)'),
    ('mwagleam_dr1_147-154', 'MWA GLEAM DR1 147-154'),
    ('mwagleam_dr1_154-162', 'MWA GLEAM DR1 154-162'),
    ('mwagleam_dr1_162-170',' MWA GLEAM DR1 162-170'),
    ('mwagleam_dr1_170-177', 'MWA GLEAM DR1 170-177'),
    ('mwagleam_dr1_170-231', 'MWA GLEAM DR1 170-231 (white)'),
    ('mwagleam_dr1_177-185', 'MWA GLEAM DR1 177-185'),
    ('mwagleam_dr1_185-193', 'MWA GLEAM DR1 185-193'),
    ('mwagleam_dr1_193-200', 'MWA GLEAM DR1 193-200'),
    ('mwagleam_dr1_200-208', 'MWA GLEAM DR1 200-208'),
    ('mwagleam_dr1_208-216', 'MWA GLEAM DR1 208-216'),
    ('mwagleam_dr1_216-223', 'MWA GLEAM DR1 216-223'),
    ('mwagleam_dr1_223-231', 'MWA GLEAM DR1 223-231'),
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
