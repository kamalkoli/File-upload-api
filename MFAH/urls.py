from django.contrib import admin
from django.urls import path
from account.views import MegazineCategoriesView, MegazineDetailsView, MegazinePagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadCategories/', MegazineCategoriesView.as_view()),
    path('uploadDetails/', MegazineDetailsView.as_view()),
    path('uploadPages/', MegazinePagesView.as_view()),
]
#Updated