from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Handles the new user's email and password to create their account.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


"""
The login_required decorator ensures only those users who are logged in can see their profile.
"""


@login_required(login_url='/login/')
def profile(request):
    """
    Renders the profile page.
    :param request:
    :return:
    """
    return render(request, 'profile.html')


def login(request):
    """
    This method checks for post method and if not displays a an empty login form. If it is a POST then the form is
    populated and checked for validity before authentication.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    """
    Logs user out by destroying login session.
    :param request:
    :return:
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
