from django.contrib import admin
from .models import Faq, Answer, Inquiry
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Answer
    model = Inquiry


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'subject',
                    'create_date', 'updated_at')
    inlines = [CommentInline]


admin.site.register(Inquiry)
# admin.site.register(Question)
admin.site.register(Answer)
