from django import forms
from crispy_forms.helper import FormHelper 


class ContactForm(forms.Form):
	email = forms.EmailField(label='E-Mail', required=True)
	body = forms.CharField()
	post = forms.CharField()
	 