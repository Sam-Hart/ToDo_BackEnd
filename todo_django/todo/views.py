# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework import viewsets
from serializers import ToDoItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from models import ToDoItem
from forms import RegistrationForm
from permissions import BelongsToUser


# Create your views here.
class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ToDoItems to be CRUDed
    """
    serializer_class = ToDoItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, BelongsToUser,)

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    """
    API endpoint to register a new user.
    """
    try:
        payload = json.loads(request.body)
    except ValueError:
        return JsonResponse(
            {"error": "Unable to parse request body"},
            status=400
        )

    form = RegistrationForm(payload)

    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data["username"],
                                        form.cleaned_data["email"],
                                        form.cleaned_data["password"])
        user.save()

        return JsonResponse({"success": "User registered."}, status=201)

    return HttpResponse(
        form.errors.as_json(),
        status=400,
        content_type="application/json"
    )
