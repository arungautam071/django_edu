from django.contrib import admin

from main_section.models import Contact

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'email','phone_number', 'Subject', 'message']