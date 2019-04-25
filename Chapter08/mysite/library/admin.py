from django.contrib import admin

# Register your models here.
from .models import Author, Book


class BookInLine(admin.TabularInline):
    model = Book
    extra = 1

    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date']})
    ]


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLine]


admin.site.register(Author, AuthorAdmin)
