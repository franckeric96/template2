from django.db import models

# Create your models here.
class Acceuil(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Acceuil')
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Acceuil'
        verbose_name_plural = 'Acceuils'

    def __str__(self):
        return self.titre
    
class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/Artiste')
    bio = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Artiste'
        verbose_name_plural = 'Artistes'

    def __str__(self):
        return self.nom
    
class Galerie(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Galerie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Galerie'
        verbose_name_plural = 'Galeries'

    def __str__(self):
        return self.titre
    
class Playlist(models.Model):
    nom_artiste = models.CharField(max_length=255)
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.nom_artiste