from django import forms
from .models import URL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class URLform(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url', 'alias']
        widgets = {
            'original_url': forms.URLInput(attrs={'placeholder': 'Enter the URL to shorten'}),
            'alias': forms.TextInput(attrs={'placeholder': 'Enter a custom alias (must be unique)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Shorten'))