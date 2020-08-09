from django.forms import ModelForm
from .models import Post

class ContactForm(ModelForm): 
	# post = forms.CharField()

	class Meta:
		model = Post
		fields = ('name','email')

def __init__(self, *args, **kwargs):
    super(MyForm, self).__init__(*args, **kwargs)
    for key, field in self.fields.items():
        if isinstance(field.widget, forms.TextInput) or \
            isinstance(field.widget, forms.Textarea) or \
            isinstance(field.widget, forms.DateInput) or \
            isinstance(field.widget, forms.DateTimeInput) or \
            isinstance(field.widget, forms.TimeInput):
            field.widget.attrs.update({'placeholder': field.label})