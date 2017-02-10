from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.db import models



class MyStore(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


