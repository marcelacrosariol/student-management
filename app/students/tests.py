from django.test import TestCase

from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import Student


class VesselTestCase(APITestCase):
    def setUp(self):
        self.list_url = 'student_list'
        self.create_url = 'student_create'

        self.valid_payload = {
            'name': 'Marcela',
            'family_name': 'Crosariol',
            'birthday': '1994-09-28',
            'student_id': '2021010001SP'
        }
        self.empty_payload = {}

    def test_student_list(self): 
        response = self.client.get(
            reverse(self.list_url)
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_valid_create_student(self):
        response = self.client.post(
            reverse(self.create_url),
            self.valid_payload
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_empty_create_student(self):
        response = self.client.post(
            reverse(self.create_url),
            self.empty_payload
        )
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
