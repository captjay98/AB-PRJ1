from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    """A User Manager derived froM
    the BaseUserManager"""

    def create_user(
        self,
        first_name,
        last_name,
        email,
        username,
        password=None,
    ):
        """Handles creation of other users"""
        if not email:
            raise ValueError("Email Required")
        if not username:
            raise ValueError("Username Required")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """Handles creation of SuperUser"""
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    A custom User class
    derived from Abstract Base User
    uses the  EMAIL for login
    instead of username
    """

    first_name = models.CharField(verbose_name="first name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)

    is_seeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    hide_email = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_username(self):
        return self.email
