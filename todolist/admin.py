from . import models
from django.contrib import admin
class TodoListAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ("title","content" ,"status", "created", "due_date")
    def download_csv(self, request, queryset):
        import csv
        f = open('stayabode_todo.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(["title","content" ,"status", "created", "due_date"])
        for s in queryset:
            writer.writerow([s.title, s.content, s.status, s.created, s.due_date])
    download_csv.short_description = "Download CSV file for selected stats."
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Status, StatusAdmin)