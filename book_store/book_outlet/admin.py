from django.contrib import admin

# Register your models here.

from .models import *

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    # list_display = ('title', 'rating', 'author', 'is_bestseller')
    # search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author',)
    
admin.site.register(Book, BookAdmin)