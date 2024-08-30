from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings


# Create users class #####################################################################
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
#########################################################################################


class Bookmark(models.Model):
    book = models.PositiveSmallIntegerField()
    page = models.PositiveSmallIntegerField()
    userId = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f"Bookmark for {self.book} on page {self.page}" 

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    userreads = models.ForeignKey('Bookmark', on_delete=models.CASCADE, default=None, null=True, blank=True) 

    def __str__(self) -> str:
        return self.email

class Book(models.Model):
    bookTitle = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.bookTitle
    

class Book_Description(models.Model): 
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers", default='')
    FANTASY_TYPES = [
        ("EPIC", "Epic Fantasy"),
        ("SCIFI", "Sci Fi"),
    ]
    type = models.CharField(max_length=5, choices=FANTASY_TYPES, default='EPIC')
    bookContent = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
