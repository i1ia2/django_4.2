import articles.models
from .models import Article, Scope, Tag

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, inlineformset_factory


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_entry = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                main_entry += 1
        if main_entry > 1:
            raise ValidationError('Укажите один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


    # TagFormSet = inlineformset_factory(articles.models.Scope, articles.models.Tag, formset=RelationshipInlineFormset)
    # inlines = [RelationshipInlineFormset]