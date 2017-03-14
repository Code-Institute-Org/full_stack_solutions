from models import User


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        """
        Get an instance of User using the supplied email and check its password
        :param email:
        :param password:
        :return:
        """

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by the django authentication system to retrieve an instance of User
        :param user_id:
        :return:
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
