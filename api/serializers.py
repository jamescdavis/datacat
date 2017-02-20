from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Dataset, Publication, DatasetPublication

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DatasetPublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatasetPublication
        fields = ('id', 'publication', 'link_time')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    datasetpublication_set = DatasetPublicationSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = ('id', 'url', 'title', 'publications', 'datasetpublication_set')

class PublicationDatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatasetPublication
        fields = ('id', 'dataset', 'link_time')

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    datasetpublication_set = PublicationDatasetSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ('id', 'doi', 'title', 'datasets', 'datasetpublication_set')
