from django.contrib import admin as defAdmin

# from django.contrib.admin.sites import AdminSite
from .models import Question

# Register your models here.
defAdmin.site.register(Question)