from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from lab3.models import Post, Comment, UserProfile


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at")
    list_filter = (('created_at', DateRangeFilter), ('created_at', DateTimeRangeFilter))
    search_fields = ("title", "content",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at")

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

admin.site.register(Comment, CommentAdmin)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
admin.site.register(UserProfile, UserProfileAdmin)
