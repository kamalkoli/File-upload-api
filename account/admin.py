from django.contrib import admin
from .models import MegazineCategories, MegazineDetails, MegazinePages, User

# Register your models here.
admin.site.register(User)
admin.site.register(MegazineDetails)
admin.site.register(MegazineCategories)
admin.site.register(MegazinePages)