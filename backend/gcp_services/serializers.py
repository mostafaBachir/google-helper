from rest_framework import serializers
from .models import *
class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    categorie = serializers.SlugRelatedField(
        read_only=True,
        slug_field='titre'
    )
    mots_cles = serializers.SerializerMethodField()
    def get_mots_cles(self, obj):
        # Récupère uniquement les titres des mots-clés associés
        return [mot_cle.titre for mot_cle in obj.mots_cles.all()]    
    class Meta:
        model = Service
        fields = ['url','id','categorie','titre','description','mots_cles']

class ProprieteServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProprieteService
        fields = ['id','titre','description']
class CasUtilisationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasUtilisationService
        fields = ['id','titre','description']
class TarificationsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarificationsService
        fields = ['id','titre','description']
class MotClesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotCles
        fields = ['id','titre']  
class ServiceDetailSerializer(serializers.HyperlinkedModelSerializer):
    categorie = serializers.SlugRelatedField(
        read_only=True,
        slug_field='titre'
    )
    proprietes = ProprieteServiceSerializer(many=True, read_only=True)
    use_cases = CasUtilisationServiceSerializer(many=True, read_only=True)
    tarifications = TarificationsServiceSerializer(many=True, read_only=True)
    mots_cles = serializers.SerializerMethodField()
    def get_mots_cles(self, obj):
        # Récupère uniquement les titres des mots-clés associés
        return [mot_cle.titre for mot_cle in obj.mots_cles.all()]
    class Meta:
        model = Service
        fields = ['url','id','categorie','titre','description','proprietes','use_cases','tarifications','mots_cles']
 