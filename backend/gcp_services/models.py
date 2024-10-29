from django.db import models

class AwsNiveau (models.Model):
    LEVEL_CHOICES = [
        (1, 'Fondamental'),
        (2, 'Associate'),
        (3, 'Professionnel'),
        (4, 'Spécialité'),
    ]

    status = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    description = models.TextField(null=True, blank=True)
    prerequis = models.CharField(null=True, blank=True, max_length=255)
    def __str__(self):
        # Utilise get_status_display pour afficher le niveau sous forme de texte
        return f"{self.get_status_display()} - {self.description[:30]}..." if self.description else self.get_status_display()

class AwsCertifications(models.Model):
    titre = models.CharField(null=True, blank=True, max_length=255)
    niveau = models.ForeignKey(AwsNiveau, null=True, blank=True, on_delete=models.SET_NULL, related_name='certifications')
    badge = models.ImageField(upload_to='badges')
    def __str__(self):
        # Affiche d'abord le niveau, suivi du titre de la certification
        niveau_display = self.niveau.get_status_display() if self.niveau else "Niveau inconnu"
        titre_display = self.titre if self.titre else "Titre inconnu"
        return f"{niveau_display} - {titre_display}"
class Categorie(models.Model):
    titre = models.CharField(null=True, blank=True, max_length=255)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.titre)


class Service(models.Model):
    titre = models.CharField(null=True, blank=True, max_length=255)
    langue = models.CharField(null=True, blank=True, max_length=255)
    categorie = models.ForeignKey(
        Categorie, null=True, blank=True, on_delete=models.SET_NULL, related_name='services')
    certification = models.ManyToManyField(AwsCertifications, blank=True, related_name='services')
    petite_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.titre)


class ProprieteService(models.Model):
    service = models.ForeignKey(
        Service, null=True, blank=True, on_delete=models.SET_NULL, related_name='proprietes')
    certification = models.ManyToManyField(AwsCertifications, blank=True,  related_name='proprietes')

    titre = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.titre)


class CasUtilisationService(models.Model):
    service = models.ForeignKey(
        Service, null=True, blank=True, on_delete=models.SET_NULL, related_name='use_cases')
    titre = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    examples = models.TextField(null=True, blank=True)
    certification = models.ManyToManyField(AwsCertifications, blank=True, related_name='use_cases')

    def __str__(self):
        return str(self.titre)

class TarificationsService(models.Model):
    service = models.ForeignKey(Service, null=True, blank=True,
                                on_delete=models.SET_NULL, related_name='tarifications')
    titre = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    certification = models.ManyToManyField(AwsCertifications, blank=True, related_name='tarifications')

    def __str__(self):
        return str(self.titre)


class MotCles(models.Model):
    service = models.ManyToManyField(
        Service, blank=True, related_name='mots_cles')
    titre = models.CharField(null=True, blank=True, max_length=255)
    certification = models.ManyToManyField(AwsCertifications, blank=True, related_name='mots_cles')

    def __str__(self):
        return str(self.titre)
