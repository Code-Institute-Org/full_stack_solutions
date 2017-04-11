from django.conf.urls import url
from todo.views import TodoView

urlpatterns = [
    url(r'^$', TodoView.as_view()),
    url(r'(?P<pk>[0-9]+)/$/', TodoView.as_view())
]