from django.db import models
from service.models import Cours
# Create your models here.

class Programme(models.Model):
    titre = models.CharField(max_length=70)
    image = models.ImageField(upload_to='image')
    description = models.TextField()
    nbr_diplome = models.IntegerField()
    
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'
        def __str__(self):
            return self.nom



class Etudiant(models.Model):
    nom = models.CharField(max_length=40)
    cours_suivie = models.ManyToManyField(Cours, related_name='Etudiant')
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Etudiant'
        verbose_name_plural = 'Etudiants'
    def __str__(self):
        return self.nom


class Teacher(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=250)
    image = models.ImageField()
    cours_dispancer = models.ManyToManyField(Cours, related_name='Teacher')
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=250)
    image = models.ImageField()
    cours = models.ManyToManyField(Cours, related_name='Teacher')
    message = models.TextField()
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
    def __str__(self):
        return self.nom