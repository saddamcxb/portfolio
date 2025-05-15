from django.contrib import admin
from .models import Contact, Education, Profile
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Education)
admin.site.register(Profile)

