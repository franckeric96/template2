from django.db import models

# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom
    
    
class Newletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newletter'
        verbose_name_plural = 'Newletters'

    def __str__(self):
        return self.email
    
