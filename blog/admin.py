from django.contrib import admin
from .models import Post,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title','author','status','counted_views','published_date')
    list_filter = ('status','author')
    #ordering = ['-created_date']
    search_fields = ['title', 'status','counted_views','published_date']
admin.site.register(Category)
admin.site.register(Post,PostAdmin)