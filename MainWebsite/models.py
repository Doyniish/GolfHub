from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Users.models import Groups


class GolfEvent(models.Model):
        datetime = models.DateTimeField()
        location = models.CharField(max_length=1000)
        group = models.OneToOneField(Groups)