from django.db import models

class Actualite(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/Actualite")
    description = models.TextField()
    date = models.DateField()
    comentaire = models.IntegerField()
    vue = models.IntegerField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Actualite'
        verbose_name_plural = 'Actualites'

    def __str__(self):
       return self.nom

class Programme(models.Model):

    titre = models.CharField(max_length=70)
    image = models.ImageField(upload_to='image/Programme')
    description = models.TextField()
    nbr_diplome = models.IntegerField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

    def __str__(self):
       return self.titre


class Etudiant(models.Model):

    nom = models.CharField(max_length=40)
    cours_suivie = models.ManyToManyField(Cours, related_name='Etudiant')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
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
    cours = models.ManyToManyField(Cours, related_name='Commentaire')
    message = models.TextField()
    
    date_update = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.nom

class Cours(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/cours")
    prix = models.FloatField()
    duree = models.DurationField()
    nbr_chap = models.IntegerField()
    description = models.TextField()
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='Cours')
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='Cours')
    prof = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Cours')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
    def __str__(self):
        return self.nom
