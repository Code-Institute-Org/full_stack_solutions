from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """
    Creates a User Creation Form
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        """
        As we don't want to display all fields we use a Meta class to include and exclude fields.
        """
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']

    def clean_password2(self):
        """
        This custom method cleans the data and checks it's validity.
        :return:
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        """
        Overrides the default save method.
        """
        instance = super(UserRegistrationForm, self).save(commit=False)

        # Automatically set to email address to create a unique identifier as the field cannot be left empty on save.
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    """
    Creates a login form.
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
