from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Groups(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=1000)
    # right now each member is comma separated
    members = models.CharField(max_length=10000)

class UserData(models.Model):
    user = models.OneToOneField(User)
    has_invite = models.BooleanField()
    # false: group, # True: event
    invite_type = models.BooleanField()
    invite_name = models.CharField()
    # every group that the user is apart of (comma separated)
    groups = models.CharField(max_length=4000)


