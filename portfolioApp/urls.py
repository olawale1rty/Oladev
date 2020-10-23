"""portfolioApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import project, blog, djrichtextfield
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import ArticleSitemap
from project.sitemaps import ProjectSitemap
from project import views

sitemaps = {
    "article": ArticleSitemap,
    "project": ProjectSitemap,
}

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('blog/', include('blog.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('pwa.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
