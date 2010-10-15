# -*- encoding:utf-8 -*-
from mock import patch, Mock

from django.test import TestCase
from django.core.urlresolvers import reverse


class SearchTestCase(TestCase):

    def test_if_search_form_is_ok(self):
        response = self.client.get(reverse('search'))

        self.assertEqual(200, response.status_code)

    @patch('youtube_search.views.__search_videos', Mock(return_value=[]))
    def test_no_videos_found(self):
        response = self.client.post(reverse('search'), {'full_text':'metallica'})

        self.assertEqual(200, response.status_code)
        self.assertTrue('videos' in response.context)
        self.assertEqual(len(response.context['videos']), 0)

    @patch('youtube_search.views.__search_videos')
    def test_no_videos_found(self, mocked_results):
        mocked_results.return_value=[('title','id')]
        response = self.client.post(reverse('search'), {'full_text':'metallica'})
        self.assertEqual(200, response.status_code)
        self.assertTrue('videos' in response.context)
        self.assertEqual(len(response.context['videos']), 1)

    def test_error_if_user_do_not_provide_full_text(self):
        response = self.client.post(reverse('search'), {'full_text':''})

        self.assertEqual(200, response.status_code)
        self.assertFalse(response.context['form'].is_valid())
