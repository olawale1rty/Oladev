from django.db import models
from django.urls import reverse

# Create your models here.

class SiteDetail(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000)
	keywords = models.CharField(max_length = 500)
	name = models.CharField(max_length = 100)
	site_slider = models.CharField(max_length = 500)
	address = models.TextField()
	site_email = models.EmailField()

	def __str__(self):
		return self.name

class PhoneNumber(models.Model):
	name = models.CharField(max_length = 70)
	phone_number = models.CharField(max_length = 14)
	site = models.ForeignKey(SiteDetail, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

class SiteSocial(models.Model):
	socials = (
		('facebook','Facebook'),
		('instagram','Instagram'),
		('twitter','Twitter'),
		('whatsapp','WhatsApp'),
		('linkedin','LinkedIn'))
	site = models.ForeignKey(SiteDetail, on_delete = models.CASCADE)
	github = models.URLField(default='https://github.com/olawale1rty')
	social_media = models.CharField(max_length = 50, choices = socials)
	link = models.URLField()

	def __str__(self):
		return self.social_media

class About(models.Model):
	image = models.ImageField(upload_to='about/images/', blank = True)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	description_two = models.CharField(max_length=250)
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	degree = models.CharField(max_length=250)
	freelance = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "About"

class Counts(models.Model):
	happy_clients = models.CharField(max_length=100)
	projects = models.CharField(max_length=100)
	hours_of_support = models.CharField(max_length=100)
	years_of_experience = models.CharField(max_length=100)

	def __str__(self):
		return "counts {}".format(self.projects)

	class Meta:
		verbose_name_plural = "Counts"

class SkillsLeft(models.Model):
	name = models.CharField(max_length=30)
	percent = models.CharField(max_length=5)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "SkillsLeft"

class SkillsRight(models.Model):
	name = models.CharField(max_length=30)
	percent = models.CharField(max_length=5)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "SkillsRight"

class Testimonials(models.Model):
	name = models.CharField(max_length=50)
	title  = models.CharField(max_length=50)
	testimony = models.TextField()
	picture = models.ImageField(upload_to='testimonials/images', blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Testimonials"

class Education(models.Model):
	title = models.CharField(max_length=30)
	years = models.CharField(max_length=30)
	school_name = models.CharField(max_length=100)
	details = models.TextField()

	def __str__(self):
		return self.title

class Summary(models.Model):
	name = models.CharField(max_length=50)
	details = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Summaries"

class SummaryList(models.Model):
	summary = models.ForeignKey(Summary, on_delete = models.CASCADE)
	list_detail = models.TextField()
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Experience(models.Model):
	name = models.CharField(max_length=50)
	years = models.CharField(max_length=50)
	details = models.TextField()

	def __str__(self):
		return self.name

class ExperienceList(models.Model):
	summary = models.ForeignKey(Experience, on_delete = models.CASCADE)
	list_detail = models.TextField()
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=50)
	filters = models.CharField(max_length=50)
	tagline = models.CharField(max_length=100)
	image = models.ImageField(upload_to='project/images/')
	url = models.URLField(blank=True)
	image_1 = models.ImageField(upload_to='project/images/', blank=True)
	image_2 = models.ImageField(upload_to='project/images/', blank=True)
	image_3 = models.ImageField(upload_to='project/images/', blank=True)
	stack = models.CharField(max_length=150)
	category = models.CharField(max_length=50)
	client = models.CharField(max_length=100)
	p_status = (
		('publish','Publish'),
		('draft','Draft'))
	publication_status = models.CharField(max_length = 60, choices = p_status, default='draft')
	date = models.DateTimeField(auto_now_add=True)
	details = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('project:detail', kwargs={
				'project_id':self.id
		})


class Client(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	subject = models.CharField(max_length = 100)
	message = models.TextField()

	def __str__(self):
		return self.name


