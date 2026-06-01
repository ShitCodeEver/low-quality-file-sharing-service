from django.contrib import admin
from .models import MediaPost

@admin.register(MediaPost)

class AdminMediaPost(admin.ModelAdmin):
    list_display = ['name', 'slug', 'media', 'extension']
    exclude = ['name', 'slug', 'extensions']
# Register your models here.
