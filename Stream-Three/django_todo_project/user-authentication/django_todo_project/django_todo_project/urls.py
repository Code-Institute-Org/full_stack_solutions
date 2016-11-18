"""django_todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from todo.views import TodoView
from accounts.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/$', TodoView.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', TodoView.as_view()),
    url(r'^accounts/register/$', RegistrationView.as_view()),
    url(r'^accounts/api-token-auth/$', obtain_jwt_token)
]
