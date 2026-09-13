from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'category', 'created_at', 'publish_date']
    fields = ['title', 'category', 'author', 'content', 'image', 'status', 'publish_date']
    list_filter = ('status','category')
    search_fields = ['title', 'content']

admin.site.register(Category)