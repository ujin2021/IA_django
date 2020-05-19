from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    #path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/', views.YearArchive.as_view(), name='year_archive'),
    path('articles/<int:year>/<int:month>/', views.MonthArchive.as_view(), name='month_archive'),
    # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]