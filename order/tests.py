from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FlavorViewSetTestCase(APITestCase):
    def test_flavors_list(self):
        response = self.client.get(reverse('flavors-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CustomerViewSetTestCase(APITestCase):
    def test_customers_list(self):
        response = self.client.get(reverse('customers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customers_create(self):
        data = {
            "full_name": "John Doe",
            "phone_number": "+49 30 9999 9999",
            "email": "johndoe@mail.com",
            "address": "123 Main St",
            "city": "Berlin",
            "state_province": '',
            "country": "Germany",
            "postal_code": "000"
        }
        response = self.client.post(reverse('customers-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
