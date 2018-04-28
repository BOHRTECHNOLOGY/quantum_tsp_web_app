from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class TSP_log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nodes = JSONField(null=True)
    first_node = models.IntegerField(null=True)
    processing_time = models.IntegerField(null=True)
