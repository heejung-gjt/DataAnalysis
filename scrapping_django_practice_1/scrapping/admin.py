from django.contrib import admin
from .models import Press, Category, Article
# Register your models here.

# admin.site.register(InsightNews)
admin.site.register(Press)
admin.site.register(Category)
admin.site.register(Article)
