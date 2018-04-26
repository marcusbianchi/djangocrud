from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import People
import json

class ModelTestCase(TestCase):
    """This class defines the test suite for the People model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.person = "Marcus"
        self.email = "marcus.santos@integradora.com.br"
        self.department = "IT"
        self.People = People(person=self.person, email=self.email,department=self.department)

    def test_model_can_create_a_person(self):
        """Test the person model can create a person."""
        old_count = People.objects.count()
        self.People.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewsTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""

        # Initialize client and force it to use authentication
        self.client = APIClient()

        # Since user model instance is not serializable, use its Id/PK
        self.people_data = {'person': 'marcus', 'email': "marcus.santos@integradora.com.br","department":"IT"}
        self.response = self.client.post(
            reverse('create'),
            self.people_data,
            format="json")

    def test_api_can_create_a_person(self):
        """Test the api has people creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_person(self):
        """Test the api can get a given people."""
        people = People.objects.filter(person="marcus").first()
        response = self.client.get(
            '/people/',
            kwargs={'pk': people.id})
        responseObject = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(responseObject[0]['id'], people.id)
    
    def test_api_can_update_person(self):
        """Test the api can update a given person."""
        people = People.objects.get()
        change_people = {'person': 'teste', 'email': "marcus.santos@integradora.com.br","department":"IT"}
        res = self.client.put(
            reverse('details', kwargs={'pk': people.id}),
            change_people, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_person(self):
        """Test the api can delete a person."""
        people = People.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': people.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
