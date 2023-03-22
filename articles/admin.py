from django.contrib import admin

from .models import Article, Scope


class RelationshipInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]