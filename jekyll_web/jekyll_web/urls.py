from django.urls import path
from app import views
from django.contrib import admin


urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r"^$", views.index, name="index"),
    path(r"^accounts/login/", views.user_login, name="login"),
    path(r"^accounts/logout/", views.user_logout, name="logout"),
    path(r"^articles/$", views.article_list, name="article-list")
    # path(r'^(?P<username>\w+)/blog/', include('foo.paths.blog')),
    # path(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
]
