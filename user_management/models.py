from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
#from djangotoolbox.fields import ListField
#from djongo import models
from django import forms
#from djongo.models.fields import ArrayField
from django.contrib.postgres.fields import ArrayField



class UserManager(BaseUserManager):


    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a `User` with an email, username and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser, models.Model):

    
    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
        )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=100 )
    
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ('email','password', )

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):

        return self.username

    @property
    def token(self):

        return self._generate_jwt_token()

    @property
    def get_full_name(self):

        return self.username

    @property
    def get_short_name(self):

        return self.username

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
        
        
    class Meta:
        app_label = 'user_management'
