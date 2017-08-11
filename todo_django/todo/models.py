# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDoItem(models.Model):
    """
    An item to be done
    """

    user = models.ForeignKey(User)
    label = models.CharField(max_length=512)
    text = models.TextField(null=True)
    done = models.BooleanField(default=False)

    class JSONAPIMeta:
        resource_name = "todos"
