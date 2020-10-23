
from django import forms
from django.forms import ModelForm
from project.models import Client

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		widgets = {
		'name': forms.TextInput(attrs = {
			'class':'form-control',
			'placeholder':'Your Name',
			'name':'name',
			'id': 'name',
			'data-rule': 'minlen:4',
			'data-msg': 'Please enter at least 4 chars'
			}),
		'email': forms.EmailInput(attrs = {
			'class':'form-control',
			'placeholder':'Your Email',
			'name':'email',
			'id': 'email',
			'data-rule': 'email',
			'data-msg': 'Please enter a valid email'
			}),
		'subject': forms.TextInput(attrs = {
			'class':'form-control',
			'placeholder':'Subject',
			'name':'subject',
			'id': 'subject',
			'data-rule': 'minlen:4', 
			'data-msg': 'Please enter at least 8 chars of subject'
			}),
		'message': forms.Textarea(attrs = {
			'class':'form-control',
			'placeholder':'Message',
			'name':'message',
			'rows': '5',
			'data-rule': 'required',
			'data-msg': 'Please write something for us'
			}),
		}
