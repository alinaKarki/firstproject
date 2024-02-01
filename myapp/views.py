from django.shortcuts import render

from myapp.models import Student

# Create your views here.

def home(request, *args, **kwargs):
	obj = Student.objects.get(id=kwargs.get('pk'))
	return render(request, 'home.html', context={'data':obj})

def listpage(request):
	obj = Student.objects.all()
	return render(request, 'list.html', context={'datas':obj})
