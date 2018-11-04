from django.db import models
from remote_imaging_micro_service.fetch_options import gleam_options

OUTPUT_TYPE_CHOICES = (
    ('fits', 'FITS'),
    ('png', 'PNG'),
    ('jpeg', 'JPEG'),
)


class CutoutQuery(models.Model):
    ra = models.FloatField(
        max_length=30,
    )

    dec = models.FloatField(
        max_length=30,
    )

    radius = models.FloatField()

    bands = models.CharField(
        max_length=25,
        choices=gleam_options(),
        default=None,
    )

    # TODO: Validation
    output_type = models.CharField(
        max_length=len(OUTPUT_TYPE_CHOICES),
        choices=OUTPUT_TYPE_CHOICES,
        default="fits"
    )
