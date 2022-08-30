from django.db import models


class Tick(models.Model):
    data = models.DateTimeField()


class TickData(models.Model):
    tick = models.ForeignKey(Tick)
    data = models.TextField()
    seconds_to_poll = models.FloatField()
