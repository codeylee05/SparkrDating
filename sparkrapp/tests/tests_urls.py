from django.test import SimpleTestCase
from django.urls import reverse, resolve

from sparkrapp.views import index

class TestViews(SimpleTestCase):

    def test_index_url_resolves(self):

        url = reverse("index")

        self.assertEqual(resolve(url).func, index)