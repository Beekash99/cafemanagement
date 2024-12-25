from django.contrib import admin
from cafe.models import Coffee, ContactUs

# Register your models here.
@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['title','image','description','price']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['your_name', 'your_email', 'your_phone', 'message']

