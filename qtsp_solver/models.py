from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.
class TSPLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nodes = ArrayField(
        ArrayField(
            models.FloatField(null=True),
            size=2,
            null=True
        ),
        null=True
    )
    distance_matrix = ArrayField(
        ArrayField(
            models.FloatField(null=True),
            null=True
        ),
        null=True
    )
    first_node = models.IntegerField(null=True)
    processing_time = models.IntegerField(null=True)
    solution = ArrayField(models.IntegerField(null=True), null=True)
    steps = models.IntegerField(null=True)
    tol = models.IntegerField(null=True)
    distribution = JSONField(null=True)
