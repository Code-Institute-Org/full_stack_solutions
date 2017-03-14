from django.shortcuts import render


# Create your views here.



def get_index(request):
    """
    This view renders the landing page
    """
    return render(request, 'index.html')
