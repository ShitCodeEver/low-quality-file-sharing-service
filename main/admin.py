from django.contrib import admin
from .models import MediaPost

@admin.register(MediaPost)

class AdminMediaPost(admin.ModelAdmin):
    list_display = ['name', 'slug', 'media']
    exclude = ['name', 'slug']
# Register your models here.
