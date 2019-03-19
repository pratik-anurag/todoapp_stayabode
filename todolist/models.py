from django.db import models

# Create your models here.
from django.utils import timezone
class Status(models.Model): 
    name = models.CharField(max_length=100) 
    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Status")
    def __str__(self):
        return self.name 
class TodoList(models.Model): 
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.ForeignKey(Status, default="general",on_delete=models.PROTECT) 
    class Meta:
        ordering = ["-created"] 
    def __str__(self):
        return self.title 