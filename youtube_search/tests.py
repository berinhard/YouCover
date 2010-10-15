from django.test import TestCase
from django.core.urlresolvers import reverse


class SearchTestCase(TestCase):

    def test_if_search_form_is_ok(self):
        response = self.client.get(reverse('search'))

        self.assertEqual(200, response.status_code)

    def test_redirect_user_to_youtube_search_results(self):
        response = self.client.post(reverse('search'), {'full_text':'metallica'})

        self.assertEqual(200, response.status_code)
        self.assertTrue('videos' in response.context)

    def test_error_if_user_do_not_provide_full_text(self):
        response = self.client.post(reverse('search'), {'full_text':''})

        self.assertEqual(200, response.status_code)
        self.assertFalse(response.context['form'].is_valid())
