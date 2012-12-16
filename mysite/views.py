from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.users.models import Users, Hackmes
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import datetime

def hello(request):
    return HttpResponse("Hello world")

@login_required
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

@login_required
def index(request):
    hackme_list = Hackmes.objects.all()
    return render_to_response('index.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, context_instance = RequestContext(request))