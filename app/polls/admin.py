from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # Fields to be displayed in list
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )

    # Filter selection on the right side of page
    list_filter = [
        'pub_date',
    ]

    # Search box field at top of page
    search_fields = [
        'question_text',
    ]

admin.site.register(Question, QuestionAdmin)
