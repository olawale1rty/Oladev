from django.contrib.sitemaps import Sitemap
from project.models import Project

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Project.objects.all().filter(
			publication_status  = 'publish')

    def lastmod(self, obj):
        return obj.date