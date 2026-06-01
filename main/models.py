from django.db import models
from django.utils.text import slugify
import os

class MediaPost(models.Model):
    name = models.CharField(verbose_name='название')
    slug = models.CharField(unique=True, verbose_name='URL')
    media = models.FileField(upload_to='uploads/', verbose_name='медиа')
    extension = models.CharField(max_length=10, blank=True, verbose_name='расширение')
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        
    def save(self, *args, **kwargs):
        if self.media:
            filename = os.path.splitext(os.path.basename(self.media.name))[0] #читай как хочешь :3, кароче оно просто берет имя файла и отрезает расширение
            self.extension = os.path.splitext(os.path.basename(self.media.name))[1] #возвращает расширение как я понял
            self.name = filename
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
# Create your models here.