# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings
from rest_framework import status
from rest_framework.test import force_authenticate, APIClient

def get_authenticated_client():
    User = get_user_model()
    user = User.objects.get(username='foobar')
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@override_settings(ROOT_URLCONF='main.urls')
class APITestCase(TestCase):
    fixtures = ["notes.json"]

    def test_authenticate(self):
        client = APIClient()
        response = client.post(
            reverse("auth"), {"username": "foobar", "password": "foobar"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["token"])

    def test_create_note(self):
        client = get_authenticated_client()
        response = client.post(
            reverse("note-list"),
            {"title": "Test note 4", "note": "This is a test note!"},
        )
        self.assertEqual(4, response.json()["id"])

    def test_list_notes(self):
        client = get_authenticated_client()
        response = client.get(reverse("note-list"))
        data = response.json()
        self.assertEqual(
            ["Test note 1", "Test note 2", "Test note 3"],
            [i["title"] for i in data]
        )

    def test_list_favorited_notes(self):
        client = get_authenticated_client()
        response = client.get("{}?favorited=True".format(reverse("note-list")))
        data = response.json()
        self.assertEqual(["Test note 3"], [i["title"] for i in data])

    def test_update_note(self):
        client = get_authenticated_client()
        response = client.patch(
            reverse("note-detail", args="1"),
            {"note": "This is a updated test note!", "favorited": True},
        )
        self.assertEqual(
            {"id": 1,
             "title": "Test note 1",
             "slug": "test-note-1",
             "note": "This is a updated test note!",
             "favorited": True},
            response.json()
        )

    def test_delete_note(self):
        client = get_authenticated_client()
        client.delete(reverse("note-detail", args="1"))
        response = client.get(reverse("note-list"))
        data = response.json()
        self.assertEqual(2, response.json()[0]["id"])

