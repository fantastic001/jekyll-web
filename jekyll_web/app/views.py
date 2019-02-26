
from django.http import Http404
from django.shortcuts import render
from .models import *

from django.http import HttpResponseRedirect

from pyjekyll import *

from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from jekyll_web import settings

def index(request):
    return render(request, "jekyll_web/index.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('article-list'))
            else: 
                return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()
        return render(request, "jekyll_web/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def article_list(request):
    site = JekyllSite(settings.JEKYLL_PATH)
    result = site.get_post_container().get_posts()
    return render(request, "jekyll_web/article_list.html", {"articles": result})

