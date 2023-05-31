from django.contrib import admin

# Register your models here.
from .models import Author, Book




class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "books",)
    list_filter = ('name',)
    search_fields = ['books']

    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)