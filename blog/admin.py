from django.contrib import admin
from .models import Post, Category, Aboutus

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Aboutus)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')
    list_filter = ('category','created_at')
