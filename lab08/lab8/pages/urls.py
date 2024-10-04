from django.urls import path
from . import views

urlpatterns = [
path("home", views.home_page),
path("feedback", views.CreateUserView.as_view()),
path("about", views.about_page),
path("thankyou", views.thanks_for_feedback_page)
]

