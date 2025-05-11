from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title","created_at","due_date","is_completed")
    list_filter = ["is_completed"]
    search_fields = ["title","description"]
    date_hierarchy = "created_at"