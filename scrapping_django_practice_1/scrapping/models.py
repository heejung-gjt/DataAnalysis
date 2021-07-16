from django.db import models
from config import settings
# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
    return self.name


class Press(models.Model):
  name = models.CharField(max_length=64)     

  def __str__(self):
    return self.name

class Article(models.Model):
  press = models.ForeignKey(Press, on_delete=models.CASCADE, related_name='article')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article',blank=True)
  code = models.CharField(max_length=32,blank=True)
  date = models.CharField(max_length=64,blank=True)
  date_code = models.DateTimeField(blank=True)
  preview_img = models.TextField(blank=True)
  img = models.TextField(blank=True)
  title = models.TextField(blank=True)
  content = models.TextField(blank=True)
  ref = models.URLField(blank=True) 
  
  def __str__(self):
    return f'{self.category} - {self.date_code} - {self.title}'
  class Meta:
    ordering = ['-date_code']
  

