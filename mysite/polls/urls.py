### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 4

from django.urls import path
from . import views
from .views import CustomLoginView


app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("register/", views.register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
]