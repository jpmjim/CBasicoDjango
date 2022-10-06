from django.contrib import admin

#import models
from .models import Choice, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
