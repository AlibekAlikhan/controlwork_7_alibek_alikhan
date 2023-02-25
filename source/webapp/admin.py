from django.contrib import admin

from webapp.models import Book


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "create_at", "name", "email", "is_deleted", "update_at")
    list_filter = ("id", "status", "create_at", "name", "email", "is_deleted", "update_at")
    search_fields = ("status", "text", "name", "email")
    filter = ("text", "status", "create_at", "name", "email", "update_at")
    readonly_fields = ("id", "create_at", "update_at")


admin.site.register(Book, ArticleAdmin)
