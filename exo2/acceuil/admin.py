from django.contrib import admin
from . import models

from django.utils.safestring import mark_safe



# Register your models here.
class AcceuilAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Video', {'fields': ['video']}),
        ('status', {'fields': ['status']})
    ]
    
    
    list_display = ('image_views','titre','date_add','status')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

                                                                                                                                  
    
class ArtisteAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','prenom','bio']}),
        ('Image',{'fields': ['photo']}),
        ('Status',{'fields': ['status']})

       
    ]
    
    list_display = ('nom','prenom','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
class GalerieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('status', {'fields': ['status']})
    ]
    
    
    list_display = ('image_views','titre','date_add','status')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['nom_artiste','video']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom_artiste','video','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom_artiste',)
    date_hierarchy = "date_add"
    list_display_links = ['nom_artiste']
    ordering = ['nom_artiste']
    list_per_page = 10

    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Acceuil, AcceuilAdmin)  
_register(models.Artiste, ArtisteAdmin) 
_register(models.Playlist, PlaylistAdmin)  
_register(models.Galerie, GalerieAdmin)   