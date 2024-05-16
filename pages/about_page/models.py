from django.db import models


class Dummy(models.Model):
    """
    Model Dummy of About Page.

    Fields:
    - dummy_field: Dummy field.
    """

    dummy_field = models.CharField(max_length=1)
