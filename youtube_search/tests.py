from django.test import TestCase
from django.core.urlresolvers import reverse


class SearchTestCase(TestCase):

    def test_if_search_form_is_ok(self):
        response = self.client.get(reverse('search'))

        self.assertEqual(200, response.status_code)

    def test_redirect_user_to_youtube_search_results(self):
        response = self.client.post(reverse('search'), {'full_text':'metallica'})

        self.assertEqual(302, response.status_code)
        self.assertTrue('metallica+cover' in response['Location'])
