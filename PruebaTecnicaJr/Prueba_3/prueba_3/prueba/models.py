from django.db import models

class DetailModel(models.Model):
    detalle = models.CharField(default=None, max_length=100)
