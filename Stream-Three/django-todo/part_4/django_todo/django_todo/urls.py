from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', include('django_todo.todo.urls')),
    url(r'^accounts/', include('django_todo.accounts.urls'))
]