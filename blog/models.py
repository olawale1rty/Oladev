from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from djrichtextfield.models import RichTextField


# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length = 60)
	photo = models.ImageField(upload_to = 'blog/authors')
	bio = models.TextField()

	def __str__(self):
		return self.name

class Categorie(models.Model):
	article_category = models.CharField(max_length = 50)

	def __str__(self):
		return self.article_category

class ArticleQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(upload_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(author__name__icontains=query) |
                    Q(author__bio__icontains=query) |
                    Q(articletext__text__icontains=query) |
                    Q(articletext__header__icontains=query) |
                    Q(articleimage__caption__icontains=query) |
                    Q(articlevideo__caption__icontains=query) |
                    Q(comment__comment__icontains=query) |
                    Q(comment__name__icontains=query) |
                    Q(comment__email__icontains=query) |
                    Q(comment__website__icontains=query)
                    )

        return self.filter(lookup)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class Article(models.Model):
	p_status = (
		('publish','Publish'),
		('draft','Draft'))
	author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True)
	title = models.CharField(max_length = 200)
	categories = models.ManyToManyField(Categorie)
	publication_status = models.CharField(max_length = 60, choices = p_status)
	slug = models.SlugField()
	upload_date = models.DateTimeField()

	objects = ArticleManager()

	def __str__(self):
		return self.title

class ArticleText(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	header = models.CharField(max_length = 200, blank = True)
	text = RichTextField()

	def __str__(self):
		return self.article.title

class ArticleImage(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	caption = models.CharField(max_length = 200, blank = True)
	image_file = models.ImageField(upload_to = 'blog/articles/images')

	def __str__(self):
		return self.article.title

class ArticleVideo(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	caption = models.CharField(max_length = 200, blank = True)
	video_file = models.FileField(upload_to = 'blog/articles/videos')

	def __str__(self):
		return self.article.title

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	comment = models.TextField()
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	website = models.URLField(blank = True)
	upload_timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class SearchQuery(models.Model):
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

    class Meta:
        verbose_name_plural = "Search Queries"