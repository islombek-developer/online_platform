from django.contrib import admin
from .models import Comment, Course, Lesson, LikeVideo, Teacher, Program

class CommentInline(admin.StackedInline):
    model=Comment
    extra=0

class LikeInline(admin.StackedInline):
    model=LikeVideo
    extra=1


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'video', 'course','created')
    list_display_links = ('title',)
    list_editable = ('course',)
    list_filter = ('course',)
    search_fields = ('title',)
    inlines = [
        CommentInline,
        LikeInline
    ]


@admin.register(Program)
class AdminProgram(admin.ModelAdmin):
    list_display = ('name',)  
    list_display_links = ('name',)

@admin.register(Teacher)
class Adminteacher(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'program')
    list_display_links = ('first_name',)
    list_editable = ('program',)
    list_filter = ('program',)
    search_fields = ('first_name',)

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('program', 'price', 'author')
    list_display_links = ('price',)
    search_fields = ('program',)


