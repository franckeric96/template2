from django.contrib import admin

from . import models 

from django.utils.safestring import mark_safe

from action import Actions

# Register your models here.
class ArticleAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Standard', {'fields': ['contenu','categorie_article']}),
        ('Tag', {'fields': ['tag']})
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

                                                                                                                                  
    
class CategorieAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','description']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
class TagAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','description']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    
    list_display = ('nom','description','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
class CommentaireAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','email']}),
        ('Contenu',{'fields': ['article','site']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','email','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10

    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Article, ArticleAdmin)  
_register(models.Categorie, CategorieAdmin) 
_register(models.Commentaire, CommentaireAdmin)  
_register(models.Tag, TagAdmin)   