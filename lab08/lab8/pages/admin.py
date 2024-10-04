from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackView(admin.ModelAdmin):
    pass
# Register your models here.
