from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)


