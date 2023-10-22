from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Contact

class ContactApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='1234567890',
            user=self.user
        )

    def test_get_contacts(self):
        response = self.client.get('contacts')  
        self.assertIsInstance(self.user,User)
        self.assertIsInstance(self.contact,Contact)

   
    def test_update_contact(self):
        data = {
            'first_name': 'Updated',
        }
        response = self.client.patch(f'/contacts/{self.contact.pk}/update/', data, format='json') 
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.first_name, 'Updated')


    def test_delete_contact(self):
        response = self.client.delete(f'/contacts/{self.contact.pk}/delete/') 
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Contact.objects.filter(pk=self.contact.pk).exists())