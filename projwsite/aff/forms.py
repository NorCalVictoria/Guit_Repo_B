from django import forms


class ContactForm(forms.Form):
	email = forms.EmailField(label='E-Mail', required=True)
	body = forms.CharField()
	post = forms.CharField()
	 