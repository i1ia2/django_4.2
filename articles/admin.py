from django.contrib import admin

from .models import Article, Scope

# class RelationshipInlineFormset(BaseInlineFormSet):
    # def clean(self):
    #     for form in self.forms:
    #         # В form.cleaned_data будет словарь с данными
    #         # каждой отдельной формы, которые вы можете проверить
    #         form.cleaned_data
    #         # вызовом исключения ValidationError можно указать админке о наличие ошибки
    #         # таким образом объект не будет сохранен,
    #         # а пользователю выведется соответствующее сообщение об ошибке
    #         raise ValidationError('Тут всегда ошибка')
    #     return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    # formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

