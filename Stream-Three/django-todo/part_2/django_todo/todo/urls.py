from django.conf.urls import url
from todo.views import TodoView

urlpatterns = [
    url(r'^$', TodoView.as_view())
]