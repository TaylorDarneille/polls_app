from django.contrib import admin
from .models import Question, Choice

# Change the title of the admin panel
admin.AdminSite.site_header = 'My Super Awesome Admin Panel!'

# Change the order of the entries
# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question_text']

# Note - you can use StackedInline instead of TabularInline
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

# Make fieldsets
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Question Information', {'fields': ['question_text']}),
		('Date and Time Stuff', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInLine]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)