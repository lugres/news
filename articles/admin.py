from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = [
        "title",
        "body"[:50],
        "author",
        "date",
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
