from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from core.models import Course, Certificate, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at',)

@admin.register(Course)
class CourseAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'title', 'status', )
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('status',)
    # history_list_display = ('id', 'status', 'title','categories__all')

@admin.register(Certificate)
class CertificateAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'user', 'course')
    # search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('user', 'course')
    history_list_display = ('id', 'user', 'course')
