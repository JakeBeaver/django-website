from django.shortcuts import render_to_response
from forms import PostingForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from page.models import posts
from django.contrib import auth
from django.contrib.auth.models import User


def create(request):
	if request.POST:
		form = PostingForm(request.POST)
		if form.is_valid() and request.user.is_authenticated():
			obj = form.save(commit=False)
			obj.username = request.user
			obj.save()
	return HttpResponseRedirect('/%s'% request.user.username)
	
def home(request):
	if request.user.is_authenticated():
		args = {}
		args.update(csrf(request))
		args['form'] = PostingForm()
		args['posts'] = posts.objects.all()
		args['user'] = request.user
		args['users'] = User.objects.all()
		return render_to_response('profile.html', args )
	else:
		return HttpResponseRedirect('/accounts/login/')
		
def profile(request, name):
	if request.user.is_authenticated():
		args = {}
		args.update(csrf(request))
		args['form'] = PostingForm()
		args['posts'] = posts.objects.filter(username=name)
		args['user'] = request.user
		args['users'] = User.objects.all()
		return render_to_response('profile.html', args )
	else:
		return HttpResponseRedirect('/accounts/login/')
