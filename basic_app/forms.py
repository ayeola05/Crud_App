from django.forms import ModelForm
from basic_app.models import School
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SchoolCreateForm(ModelForm):
	class Meta:
		model = School
		fields = '__all__'

class SchoolUpdateForm(ModelForm):
	class Meta:
		model = School
		fields = ['name', 'principal'] 


class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
