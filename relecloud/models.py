from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )

    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,

    )

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={"pk":self.pk})