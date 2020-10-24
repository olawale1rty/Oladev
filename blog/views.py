from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from project.models import SiteDetail
from blog.models import Article, SearchQuery
from blog.models import Comment as Cmt
from blog.models import Categorie as BlogCategory
from blog.forms import CommentForm
from django.core.paginator import (Paginator, 
								   EmptyPage, 
								   PageNotAnInteger)

# Create your views here.
################################
#
#
#   CUSTOM FUNCTION AND CLASSES
#
################################
def auto_paginate(queryset, request, get_arg = 'page',paginate_by = 10):
	page = request.GET.get(get_arg, 1)
	paginator = Paginator(queryset, paginate_by)
	try:
		return paginator.page(page)
	except PageNotAnInteger:
		return paginator.page(1)
	except EmptyPage:
		return paginator.page(paginator.num_pages)
###########
#
#
#   END
#
#
###########

class Blog(View):

	def get(self, request):
		context = {}
		articles_list = Article.objects.all().filter(
			publication_status  = 'publish').order_by('-upload_date')
		context['articles'] = auto_paginate(request=request,
			queryset = articles_list , paginate_by = 3)
		context['blog_categories'] = BlogCategory.objects.all()
		context['site_details'] = SiteDetail.objects.get()
		template = 'blog/blog.html'
		return render(request, template, context)

class BlogArticle(View):

	def get(self, request, ** kwargs):
		template = 'blog/blog-detail.html'
		context = {}
		default_article = Article.objects.get(slug = kwargs['slug'])
		default_value = {'article': default_article}
		try:
			context['form_status'] = kwargs['form_status']
		except:
			pass
		context['comment_form'] = CommentForm( initial = default_value)
		context['comments'] = Cmt.objects.filter(
			article = default_article).order_by('-upload_timestamp')
		context['article'] = Article.objects.get(slug = kwargs['slug'])
		context['site_details'] = SiteDetail.objects.get()
		context['blog_categories'] = BlogCategory.objects.all()
		return render(request, template, context)

class BlogArticleCategory(View):

	def get(self, request, ** kwargs):
		context = {}
		fetch_category = kwargs['category']
		fetch_category = BlogCategory.objects.get(article_category = fetch_category)
		articles_list = Article.objects.all().filter(
			publication_status  = 'publish', categories = fetch_category).order_by('-upload_date')
		context['articles'] = auto_paginate(request=request,
			queryset = articles_list , paginate_by = 3)
		context['site_details'] = SiteDetail.objects.get()
		context['current_category'] = fetch_category
		context['blog_categories'] = BlogCategory.objects.all()
		template = 'blog/blog.html'
		return render(request, template, context)

class Comment(View):

	def get(self, request, **kwargs):
		return redirect("blog:blog_index")

	def post(self, request):
		new_comment = CommentForm(request.POST)
		if(new_comment.is_valid()):
			new_comment.save()
			return BlogArticle().get(request,
			 slug = new_comment.cleaned_data['article'].slug,
			 form_status = 'success')
		else:
			return BlogArticle().get(request,
			 slug = new_comment.cleaned_data['article'].slug,
			 form_status = 'fail')

def search_view(request):
	query = request.GET.get('q', None)
	context = {}
	context["query"] = query
	if query is not None:
		SearchQuery.objects.create(query=query)
		blog_list = Article.objects.search(query=query).filter(
			publication_status  = 'publish').order_by('-upload_date')
		context['blog_list'] = auto_paginate(request=request,
			queryset = blog_list , paginate_by = 3)
	context['site_details'] = SiteDetail.objects.get()
	context['blog_categories'] = BlogCategory.objects.all()
	return render(request, 'blog/view.html',context)