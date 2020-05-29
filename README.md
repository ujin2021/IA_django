# IA_try_django/
## <Django Tutorial - polls>
  ### commit each part of django document - making polls app
  ### django_document) https://docs.djangoproject.com/ko/3.0/intro/overview/
  
<hr>

## <Django Tutorial - news>
  
### admin.py
#### make for managing Articles and Reporters
### models.py
#### def get_absolute_url(self) - added for code conciseness(when using detail view) <br> 
### urls.py
#### localhost:8000/news/articles/ <br>
* show list of years. 
* you can move to year archives by click year. <br>
#### localhost:8000/news/articles/[year]/ <br> 
* show list of articles by year. <br>
* you can move to month archives by click month. <br>
* you can directly read article by click headline. <br>
#### localhost:8000/news/articles/[year]/[month]/ <br>
* show list of articles by month/year. <br>
* you can move to day archives by click day. <br>
* you can directly read article by click headline. <br>
#### localhost:8000/news/articles/[year]/[month]/[day]/ <br>
* show list of articles by day/month/year. <br>
* you can move to article by click headline. <br>

<hr>

### 실행 화면
#### IA_try_django/images

<hr>

### 참고 사이트
>get_absolute_url) https://wayhome25.github.io/django/2017/05/05/django-url-reverse/ <br>
>date format) https://ssungkang.tistory.com/entry/DjangoDate%EC%99%80-Time%EC%9D%84-%EB%82%98%ED%83%80%EB%82%B4%EB%8A%94-template-filter <br>
>static directory) https://velog.io/@ground4ekd/django-static
