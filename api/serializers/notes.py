# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "slug", "note", "favorited")
        read_only_fields = ("id", "slug",)

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop("user", None)
        super(NoteSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        if self._user and not validated_data.get('owner'):
            validated_data['owner'] = self._user
        return super(NoteSerializer, self).create(validated_data)
