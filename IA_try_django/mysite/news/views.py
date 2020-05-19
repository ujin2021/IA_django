from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import *

from .models import Article, Reporter


# def year_archive(request, year):
#     a_list = Article.objects.filter(pub_date__year=year)
#     context = {'year': year, 'article_list': a_list}
#     return render(request, 'news/year_archive.html', context)

# def month_archive(request, month):
#     a_list = Article.objects.filter(pub_date__year=month)
#     context = {'month': month, 'article_list': a_list}
#     return render(request, 'news/month_archive.html', context)

class YearArchive(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list=True
    template_name = 'news/year_archive.html'

class MonthArchive(MonthArchiveView):
    model = Article
    date_field = "pub_date"
    template_name = 'news/month_archive.html'