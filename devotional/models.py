""" Python Package Support """
from datetime import datetime

""" Django Package Support """
from django.db import models
from django.utils.timezone import utc

""" Internal Package Support """


"""
 
 File       :: devotional/models.py
 
 Author(s)  :: Matthew J Swann
 Version    :: 1.0
 Last Mod   :: 2014-08-11
 Mod by     :: Matthew J Swann
  
"""

#TABLE: Devotional
class Devotional(models.Model):
    title = models.CharField(max_length=128)
    month = models.IntegerField()
    day   = models.IntegerField()
    body  = models.TextField(default='')
