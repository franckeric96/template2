from django.contrib import admin

from . import models
from django.utils.safestring import mark_safe

from actions import Actions

# Register your models here.                                                                                                                                
    
class ContactAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','email']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
class NewletterAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['email']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    
    list_display = ('email','date_add','status')
    list_filter = ('status',)
    search_fields = ('email',)
    date_hierarchy = "date_add"
    list_display_links = ['email']
    ordering = ['email']
    list_per_page = 10
    


    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)
  
_register(models.Contact, ContactAdmin)  
_register(models.Newletter, NewletterAdmin)   