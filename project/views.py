from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from project.models import (
	SiteDetail,
	About,
	Counts,
	SkillsLeft,
	SkillsRight,
	Testimonials,
	Education,
	Summary,
	Experience,
	Project
	)

from project.forms import ClientForm

# Create your views here.
def index(request, ** kwargs):
	projects = Project.objects.all().filter(
			publication_status  = 'publish')
	site_details = SiteDetail.objects.get()
	client_form = ClientForm()
	about = About.objects.get()
	counts = Counts.objects.get()
	skills_right = SkillsRight.objects.all()
	skills_left = SkillsLeft.objects.all()
	testimonial = Testimonials.objects.all()
	education = Education.objects.all()
	summary = Summary.objects.all()
	experience = Experience.objects.all()


	context = { }
	context['projects'] = projects
	context['site_details'] = site_details
	context['client_form'] = client_form
	context['about'] = about
	context['counts'] = counts
	context['skills_left'] = skills_left
	context['skills_right'] = skills_right
	context['testimonial'] = testimonial
	context['education'] = education
	context['summary'] = summary
	context['experience'] = experience
	try:
		context['form_status'] = kwargs['form_status']
	except:
		pass
	return render(request, 'project/index.html', context)

def detail(request, project_id):
	site_details = SiteDetail.objects.get()
	project = get_object_or_404(Project, id=project_id)
	context = {
		'project': project,
		'site_details': site_details
	}
	return render(request, 'project/portfolio-details.html', context)

class Client(View):

	def get(self, request, **kwargs):
		return redirect("project:index")

	def post(self, request, ** kwargs):
		'''This is the view that handles
		new clients from the contact page'''
		new_client = ClientForm(request.POST)
		if(new_client.is_valid()):
			new_client.save()
			return index(request, form_status = 'success')
		else:
			return index(request, form_status = 'fail')

# from django.core.mail import send_mail

# send_mail('subject', 'body of the message', 'sender@example.com', ['receiver1@example.com', 'receiver2@example.com'])

def handler404(request, exception=None):
	context = { }
	site_details = SiteDetail.objects.get()
	context['site_details'] = site_details
	return render(request, 'project/404.html', context, status=404)

def handler500(request):
	context = { }
	site_details = SiteDetail.objects.get()
	context['site_details'] = site_details
	return render(request, 'project/500.html', context, status=500)