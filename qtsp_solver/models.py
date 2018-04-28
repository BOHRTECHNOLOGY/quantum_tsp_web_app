from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    first_node = models.IntegerField(null=True)
    processing_time = models.IntegerField(null=True)
    solution = ArrayField(models.IntegerField(null=True), null=True)
