from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from MainWebsite.models import GolfEvent


class Groups(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=1000)
    members = models.ManyToManyField(User, related_name='+')

class UserData(models.Model):
    user = models.OneToOneField(User)

    has_invite = models.BooleanField(default=False)
    # false: group, # True: event
    invite_type = models.BooleanField(default=False)
    invite_name = models.CharField(max_length=1000, default='empty')

    groups = models.ManyToManyField(Groups)
    stats = models.OneToOneField(UserStats)
    events = models.ManyToManyField(GolfEvent)

class UserStats(models.Model):
    round = models.ManyToManyField(Round)

class Round(models.Model):
    datetime = models.DateTimeField()
    front_nine = models.OneToOneField(FrontNine)
    # Null if user only played nine holes
    back_nine = models.OneToOneField(BackNine)

class FrontNine(models.Model):
    hole_one = models.IntegerField()
    hole_two = models.IntegerField()
    hole_three = models.IntegerField()
    hole_four = models.IntegerField()
    hole_five = models.IntegerField()
    hole_six = models.IntegerField()
    hole_seven = models.IntegerField()
    hole_eight = models.IntegerField()
    hole_nine = models.IntegerField()

class BackNine(models.Model):
    hole_ten = models.IntegerField()
    hole_eleven = models.IntegerField()
    hole_twelve = models.IntegerField()
    hole_thirteen = models.IntegerField()
    hole_fourteen = models.IntegerField()
    hole_fifteen = models.IntegerField()
    hole_sixteen = models.IntegerField()
    hole_seventeen = models.IntegerField()
    hole_eighteen = models.IntegerField()