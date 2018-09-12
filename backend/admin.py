from django.contrib import admin

from backend.models import Field, RiskType


class FieldInline(admin.StackedInline):
    model = Field
    extra = 2
    min_num = 1


class RiskTypeAdmin(admin.ModelAdmin):
    inlines = [FieldInline, ]


admin.site.register(RiskType, RiskTypeAdmin)
