from django.contrib import admin
from .models import Post

class PostDB(admin.ModelAdmin):
    list_display = [
        "Title", "Text", "Author", "Created_date", "Published_date"
]


# Register your models here.
admin.site.register(Post, PostDB)
