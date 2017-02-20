from django.db import models

class Dataset(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    publications = models.ManyToManyField('Publication', through='DatasetPublication')

class Publication(models.Model):
    doi = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    datasets = models.ManyToManyField('Dataset', through='DatasetPublication')

class DatasetPublication(models.Model):
    dataset = models.ForeignKey(Dataset)
    publication = models.ForeignKey(Publication)
    link_time = models.DateTimeField(None, None, True)
