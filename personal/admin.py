from django.contrib import admin
from .models import Topic

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("tagline","text", "url", "date")

