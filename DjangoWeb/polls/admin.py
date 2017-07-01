from django.contrib import admin

# from django.contrib.admin.sites import AdminSite
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
