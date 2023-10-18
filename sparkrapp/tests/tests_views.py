from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.index_url = reverse("index")

    def test_GET_index(self):

        response = self.client.get(self.index_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sparkrapp/index.html")