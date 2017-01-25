from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# Create your tests here.


class ArticleViewsTest(TestCase):

    def test_index_page(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_article_page(self):
        client = Client()
        response = client.get(reverse('article', args=[5, ]))
        self.assertEqual(response.status_code, 404)
