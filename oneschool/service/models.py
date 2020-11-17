from django.db import models
from website.models import Etudiant, Commentaire, Teacher  

# Create your models here.

class Cours(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField()
    prix = models.FloatField()
    duree = models.DurationField()
    nbr_chap = models.IntegerField()
    description = models.TextField()
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='Cours')
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='Cours')
    prof = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Cours')
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        def __str__(self):
            return self.nom