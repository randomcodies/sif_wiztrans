from django.contrib import admin

from .models import Question, Choice, authenticate,Category,Document


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['question_category1']}),
        (None,               {'fields': ['question_category2']}),
        (None,               {'fields': ['question_link']}),
        (None,               {'fields': ['question_text_my']}),
        (None,               {'fields': ['question_text_md']}),
        (None,               {'fields': ['question_text_ta']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_category1']}),
        (None,               {'fields': ['question_category2']}),
    ]
    list_display = ('question_category1', 'question_category2')
    search_fields = ['question_category1','question_category2']

admin.site.register(Category, CategoryAdmin)







