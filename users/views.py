from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
# Create your views here.
def userLogin(request):
	next = request.GET.get('next', '/warranties')
	render_template = "user_login.html"
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user=authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, render_template, {"redirect_to": next, "title": "Login"})

def userLogout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)