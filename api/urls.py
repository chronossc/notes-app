# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
import rest_framework_jwt.views

from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

router = DefaultRouter()
router.register(r"notes", NoteViewSet, base_name="note")

urlpatterns = [
    url(r'^auth/$', rest_framework_jwt.views.obtain_jwt_token),
] + router.urls
