from django.contrib import admin

from . import models 

from django.utils.safestring import mark_safe



# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
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





def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Article, ArticleAdmin)                                                                                                                                    
    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','status')
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom','description','date_add','status')
    
    
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom','email','date_add','status')
        

    
