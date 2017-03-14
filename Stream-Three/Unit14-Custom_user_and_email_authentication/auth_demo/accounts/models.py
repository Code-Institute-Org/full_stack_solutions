from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


# Create your models here.
class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password. The other attributes give default
        permissions for admin in Django.

        :param username:
        :param email:
        :param password:
        :param is_staff:
        :param is_superuser:
        :param extra_fields:
        :return:
        """

        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
        """
        Note that username=email to allow email address for login.
        """

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    # TODO: Now that we've abstracted this class we can add any number of custom attribute to our user class.
    # TODO: In future lessons we'll be adding things like payment details!

    objects = AccountUserManager()
