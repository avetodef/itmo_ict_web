from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from .forms import Form
def home_page(request):
    return render(request, "home.html")
# Create your views here.

class CreateUserView(CreateView):
    model = Feedback
    #fields = ['name', 'last_name', 'age', 'email', 'comment']
    form_class = Form
    success_url = "/thankyou"
    template_name = "feedback.html"
def about_page(request):
    return render(request, "about.html")

def thanks_for_feedback_page(request):
    return render(request, "thankyou.html")

