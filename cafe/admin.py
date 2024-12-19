from django.contrib import admin
from cafe.models import Coffee

# Register your models here.
@admin.register(Coffee)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image','description']
