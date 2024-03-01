from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body"[:50],
        "author",
        "date",
    ]


admin.site.register(Article, ArticleAdmin)
