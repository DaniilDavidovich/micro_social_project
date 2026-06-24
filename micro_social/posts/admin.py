from django.contrib import admin
from .models import Post
from .models import Group

class PostInline(admin.TabularInline):  # or admin.StackedInline
    model = Post
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text', 'title') 
    list_filter = ('pub_date',) 
    empty_value_display = '-empty-'  


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    search_fields = ('title', 'description') 
    empty_value_display = '-empty-'  
    inlines = (PostInline,)
