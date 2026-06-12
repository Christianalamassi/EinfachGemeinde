from django.contrib import admin
from .models import Pray

# Register your models here.
@admin.register(Pray)

class PrayAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    
    # Adds a search bar for these fields
    search_fields = ('email', 'first_name', 'last_name')
    
    # Adds a filter sidebar on the right
    list_filter = ('created_at',)