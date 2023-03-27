from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


class LectureAdmin(admin.TabularInline):
    model=Lecture

class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureAdmin]
    list_display = ['title', 'author', 'number_of_lectures'] 
    
    def title(self, course):
        return f'{course.title}'

    def author(self, course):
        return f'{course.author}'
        
    def number_of_lectures(self, course):
        return f'{course.number_of_lectures}'

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(FirstAid, PostAdmin)
admin.site.register(Course, CourseAdmin)
