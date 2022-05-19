from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import MegazineCategories, MegazineDetails, MegazinePages
# from django.core.files.uploadedfile import InMemoryUploadedFile


class MegazineCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=MegazineCategories
        fields = ['CategoryID','CategoryName', 'CategoryDiscription']


class MegazineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MegazineDetails
        fields = ['MegazineID', 'MegazineCover','MegazineName','MegazineDiscription','RentPrice','BuyPrice','IssueDate', 'Rating', 'Categories']



class MegazinePagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=MegazinePages
        fields = ['Megazines','MegazinePages']
