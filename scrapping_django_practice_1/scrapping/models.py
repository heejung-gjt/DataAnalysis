from django.db import models

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
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
  code = models.CharField(max_length=32)
  date = models.CharField(max_length=64)
  preview_img = models.TextField()
  img = models.TextField()
  title = models.TextField()
  content = models.TextField()
  ref = models.URLField() 
  
  def __str__(self):
    return self.title
  

