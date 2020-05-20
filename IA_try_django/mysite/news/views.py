from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import *

from .models import Article, Reporter

class Archive(ArchiveIndexView):
    model = Article
    date_field = "pub_date"
    template_name = "news/archive.html"

class ArticleDetail(DetailView):
    model = Article
    template_name = 'news/detail.html'

class YearArchive(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list=True
    template_name = 'news/year_archive.html'

class MonthArchive(MonthArchiveView):
    model = Article
    date_field = "pub_date"
    template_name = 'news/month_archive.html'
    month_format = '%m'

class DayArchive(DayArchiveView):
    model = Article
    date_field = "pub_date"
    template_name = 'news/day_archive.html'
    month_format = '%m'