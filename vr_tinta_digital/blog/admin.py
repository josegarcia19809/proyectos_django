from django.contrib import admin
from .models import Category, Article


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
