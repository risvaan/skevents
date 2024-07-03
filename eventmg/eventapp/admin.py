from django.contrib import admin
from .models import Event, Booking, Contact

# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
