from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title', 'status','counted_views','published_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title', 'status','counted_views','published_date']
admin.site.register(Post,PostAdmin)