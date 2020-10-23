from django.contrib.sitemaps import Sitemap
from blog.models import Article

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Article.objects.all().filter(
			publication_status  = 'publish').order_by('-upload_date')

    def lastmod(self, obj):
        return obj.upload_date

    def location(self, obj):
        return '/blog/article/{}'.format(obj.slug)