from django.db import models

# Create your models here.
from django.db import models
from gcp_services.models import Service
# Create your models here.
class Tutorial(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="tutorials")
    titre = models.CharField(max_length=100)
    description = models.TextField(help_text="Résumé du tutoriel")
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class TutorialSection(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="sections")
    titre = models.CharField(max_length=100)
    description = models.TextField(help_text="Description de la section")
    media = models.FileField(upload_to="tutorial_media/", blank=True, null=True)
    aws_cli_commandes = models.TextField(help_text="Commandes AWS CLI associées", blank=True, null=True)
    ordre = models.PositiveIntegerField(help_text="Ordre d'affichage de la section")

    def __str__(self):
        return f"{self.tutorial.titre} - {self.titre}"