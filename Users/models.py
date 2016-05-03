from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from MainWebsite.models import GolfEvent


################
# Group Models #
################


class Groups(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    owner = models.OneToOneField(User, related_name='+')
    members = models.ManyToManyField(User, related_name='+')


###############
# Stat Models #
###############


class FrontNine(models.Model):
    hole_scores = models.CharField(max_length=1000)
    hole_putts = models.CharField(max_length=1000)

class BackNine(models.Model):
    hole_scores = models.CharField(max_length=1000)
    hole_putts = models.CharField(max_length=1000)

class Round(models.Model):
    datetime = models.DateTimeField()
    front_nine = models.OneToOneField(FrontNine)
    # Null if user only played nine holes
    back_nine = models.OneToOneField(BackNine)

class UserStats(models.Model):
    round = models.ManyToManyField(Round)


#################
# Request Model #
#################

class Requests(models.Model):
    # false: group, # True: event
    invite_type = models.BooleanField(default=False)
    # used to reference back to the object they are being requested to be added to
    invite_object_id = models.IntegerField()
    # Name of group or event
    invite_name = models.CharField(max_length=1000, default='empty')

####################
# User Data Models #
####################


class UserData(models.Model):
    # django user model
    user = models.OneToOneField(User)
    # group and event requests
    requests = models.ManyToManyField(Requests)
    # groups the user is apart of
    groups = models.ManyToManyField(Groups)
    # user stats
    stats = models.OneToOneField(UserStats)
    # events user is going to
    events = models.ManyToManyField(GolfEvent)
