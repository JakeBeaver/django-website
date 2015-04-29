from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from accounts.forms import RegistrationForm
# Create your views here

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("login.html", c)
	
def authenticate(request):
	username =  request.POST.get('username', '')
	password =  request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect ('/accounts/loggedin/')
	else:
		return HttpResponseRedirect ('/accounts/invalid/')
		
def invalid(request):
	return HttpResponse('<meta http-equiv="refresh" content="1;url=/accounts/login/" />invalid username or password')
	
def loggedin(request):
	return HttpResponseRedirect('/')
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
	
def register_user(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return HttpResponse('<meta http-equiv="refresh" content="1;url=/"/>Registration was successfull')
		
	args = {}
	args.update(csrf(request))
	
	args['form'] = RegistrationForm()
	
	return render_to_response('register.html', args)
			
			
def register_success(request):
	return HttpResponse('user registered')
