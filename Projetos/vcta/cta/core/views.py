from django.shortcuts import render

#from .forms import UserForm, UserProfileForm

# Create your views here.

def home(request):
	return render(request, 'base.html')
