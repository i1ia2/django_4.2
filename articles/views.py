from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles_objects = Article.objects.all().order_by('-published_at')

    context = {'object_list': articles_objects}
    return render(request, template, context)