
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

@login_required
def article_read(request, article_slug):
    site = JekyllSite(settings.JEKYLL_PATH)
    result = site.get_post_container().get_post(article_slug)
    from markdown import Markdown 
    md = Markdown()
    html_contents = md.convert(result.get_contents())
    return render(request, "jekyll_web/article_view.html", {
        "article": result,
        "html_contents": html_contents
    })
@login_required
def article_edit(request, article_slug):
    form = ArticleForm()
    if article_slug != "new":
        site = JekyllSite(settings.JEKYLL_PATH)
        result = site.get_post_container().get_post(article_slug)
        form = ArticleForm(dict(title = result.get_title(), contents = result.get_contents()))
    return render(request, "jekyll_web/article_form.html", {
        "form": form,
        "slug": article_slug
    })