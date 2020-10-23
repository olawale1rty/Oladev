from  django import forms
from django.forms import ModelForm
from blog.models import (Comment)


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'
		widgets = {
			'article': forms.Select(attrs = {'id':'article',\
				'class':'comment-input-2 invisible',\
				}),
			'name': forms.TextInput(attrs = {'id':'name',\
				'class':'comment-input',\
				'placeholder':'Name *'}),
			'comment': forms.Textarea(attrs = {'id':'comment',\
				'class':'comment-input-3',\
				'placeholder':'Comment...',
				'rows':'4'}),
			'email': forms.EmailInput(attrs = {'id':'email',\
				'class':'comment-input',
				'placeholder':'Email *'}),
			'website': forms.TextInput(attrs = {'id':'website',\
				'class':'comment-input-2',
				'placeholder':'Website'})
		}
