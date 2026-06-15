from django.contrib import admin
from .models import Pray

@admin.register(Pray)
class PrayAdmin(admin.ModelAdmin):
    # Added 'phone' to the main table view
    list_display = ('first_name', 'last_name', 'created_at')
    
    # Added 'phone' and 'message' so you can search by the user's content
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'message')
    
    # Keeps date filtering and adds ability to see messages in the detail view
    list_filter = ('created_at',)
    
    # Optional: Makes the form cleaner in the admin edit page
    readonly_fields = ('created_at',)