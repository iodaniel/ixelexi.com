from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MySitemap(Sitemap):
    def items(self):
        return ['index', 'news']

    def location(self, item):
        return reverse(item)
