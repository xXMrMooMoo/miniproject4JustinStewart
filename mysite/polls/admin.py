### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 4

from django.contrib import admin
from .models import Question, Choice
from django.contrib import admin
from .models import Profile

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_count', 'last_login')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
