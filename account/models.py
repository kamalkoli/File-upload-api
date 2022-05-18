from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import uuid
from account.manager import UserManager 



class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )

    fullname = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=10, unique=True)
    tc = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    

    def name(self):
        return self.name

    def __str__(self):
        return self.email


class MegazineCategories(models.Model):
    CategoryID = models.IntegerField(primary_key=True)
    CategoryName =models.CharField(max_length=255)
    CategoryDiscription = models.CharField(max_length=500)
    
    def __str__(self):
        return self.CategoryName


class MegazineDetails(models.Model):
    MegazineID = models.IntegerField(primary_key=True)
    MegazineCover = models.ImageField(upload_to='MegazineCover')
    MegazineName =models.CharField(max_length=255)
    MegazineDiscription = models.CharField(max_length=500)
    RentPrice = models.IntegerField()
    BuyPrice = models.IntegerField()
    IssueDate = models.DateField()
    Rating = models.IntegerField()
    CategoryID = models.ForeignKey(MegazineCategories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.MegazineName


class MegazinePages(models.Model):
    MegazineID = models.ForeignKey(MegazineDetails, on_delete=models.CASCADE)
    MegazinePages = models.FileField(upload_to='Pages')

    def MegID(self):
        return self.MegazineID


