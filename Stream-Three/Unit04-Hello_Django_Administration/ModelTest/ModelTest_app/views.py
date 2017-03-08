from django.shortcuts import render
from ModelTest_app.models import Contact
from django.http import HttpResponse


# Create your views here.
def get_contacts(request):
    return render(request, "ModelTest/index.html",
                  {'contact_list': Contact.objects.all()})


def get_index(request):
    return HttpResponse('Hello World!')
