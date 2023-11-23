from django.db import models


class Dummy(models.Model):
    dummy_field = models.CharField(max_length=1)
