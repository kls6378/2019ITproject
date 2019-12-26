from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path("search/", view=views.Search.as_view(), name="search"),
]