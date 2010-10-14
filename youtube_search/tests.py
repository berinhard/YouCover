from django.test import TestCase
from django.core.urlresolvers import reverse


class SearchTestCase(TestCase):

    def test_if_search_form_is_ok(self):
        response = self.client.get(reverse('search'))

        self.assertEqual(200, response.status_code)
