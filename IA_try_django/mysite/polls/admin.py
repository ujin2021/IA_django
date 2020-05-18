from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # 입력 칸 추가(3단위로)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)