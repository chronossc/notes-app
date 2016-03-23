# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Note(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    note = models.TextField()
    favorited = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notes")


@receiver(pre_save, sender=Note)
def update_slug(sender, instance, **kwargs):
    slug = slugify(instance.title)[:50]
    existent_slug = Note.objects.filter(slug=slug)
    if existent_slug:
        slug = "{}-{}".format(slug, time.time())
    instance.slug = slug
