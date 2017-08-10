# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from models import ToDoItem
from serializers import ToDoItemSerializer

from django.shortcuts import render

# Create your views here.


class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ToDoItems to be CRUDed
    """
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
