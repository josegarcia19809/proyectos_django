from django.shortcuts import render
from blog.models import Article, Category

from blog.models import Category


# Create your views here.

def list(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles,
    })


def category(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, 'categories/category.html', {
        'category': category,
    })
