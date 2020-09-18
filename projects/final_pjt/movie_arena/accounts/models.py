from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, age, password=None):
        if not email :
            raise ValueError('must have user email')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            age = age,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, age, password ):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            age = age,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    # GENRE_CHOICES = {
    #   ('10770','TV Movie'), #오른쪽에 있는 것이 화면에 보인다.
    #   ('10752', 'War'),
    #   ('10751', 'Family'),
    #   ('10749', 'Romance'),
    #   ('10402', 'Music'),
    #   ('9648', 'Mystery'),
    #   ('878', 'Science Fiction'),
    #   ('99', 'Documentary'),
    #   ('80', 'Crime'),
    #   ('53', 'Thriller'),
    #   ('37', 'Western'),
    #   ('36', 'History'),
    #   ('35', 'Comedy'),
    #   ('28', 'Action'),
    #   ('27', 'Horror'),
    #   ('18', 'Drama'),
    #   ('16', 'Animation'),
    #   ('14', 'Fantasy'),
    #   ('12', 'Adventure'),

    # }
    color = models.CharField(max_length=80, default="white", null=True)
    red = models.IntegerField(default=0)
    grey = models.IntegerField(default=0)
    yellow = models.IntegerField(default=0)
    mint = models.IntegerField(default=0)
    skyblue = models.IntegerField(default=0)
    dark = models.IntegerField(default=0)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','age']
