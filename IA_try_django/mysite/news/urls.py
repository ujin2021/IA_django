from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('articles/', views.Archive.as_view(), name="archive"),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name="detail"),
    path('articles/<int:year>/', views.YearArchive.as_view(), name='year_archive'),
    path('articles/<int:year>/<int:month>/', views.MonthArchive.as_view(), name='month_archive'),
    path('articles/<int:year>/<int:month>/<int:day>/', views.DayArchive.as_view(), name="day_archive"),
]