from django.shortcuts import render, redirect
from basic_app.models import School, Student
from basic_app.forms import SchoolCreateForm, SchoolUpdateForm, RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):
	context = {}
	return render(request, 'basic_app/index.html', context)

def SchoolView(request):
	schools = School.objects.all()
	context = {'schools':schools}
	return render(request, 'basic_app/school_list.html', context)

def SchoolDetail(request, pk):
	schools = School.objects.get(id=pk)
	context = {'schools':schools}
	return render(request, 'basic_app/school_detail.html', context)

def SchoolCreateView(request):
	if request.method == 'POST':
		form = SchoolCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('basic_app:list')
	form = SchoolCreateForm()
	context = {'form':form}
	return render(request, 'basic_app/create.html', context)

def SchoolUpdateView(request, pk):
	schools = School.objects.get(id=pk)
	form = SchoolUpdateForm(instance=schools)

	if request.method == "POST":
		form = SchoolUpdateForm(request.POST, instance=schools)
		if form.is_valid():
			form.save()
			return redirect('basic_app:list')
	context = {'form':form}
	return render(request, 'basic_app/create.html', context)

def SchoolDeleteView(request, pk):
	school = School.objects.get(id=pk)

	if request.method == 'POST':
		school.delete()
		return redirect('basic_app:list')

	context = {'school':school}
	return render(request, 'basic_app/school_delete.html', context)

def RegisterView(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('basic_app:index')

	context = {'form':form}
	return render(request, 'basic_app/registration.html', context)