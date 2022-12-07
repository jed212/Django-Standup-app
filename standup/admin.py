from django.contrib import admin

from .models import standup, comments

admin.site.register(standup)
admin.site.register(comments)
# Register your models here.
