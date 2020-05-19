from django.db import models
from django.urls import reverse

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("news:year_archive", kwargs={"pk": self.pk})
    

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    
    def get_absolute_url(self):
        return reverse("news:year_archive", args=(self.pub_date.year,))
    