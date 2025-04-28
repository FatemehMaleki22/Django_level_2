from django import forms
from first_app.models import User

class SignupForm(forms.ModelForm):
  # first_name = forms.CharField(max_length=200)
  # last_name = forms.CharField(max_length=200)
  # email = forms.EmailField(max_length=100)
  class Meta:
    model = User
    fields = '__all__'