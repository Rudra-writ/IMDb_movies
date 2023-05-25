from django.db import models

class Movies(models.Model):
    imdb_title_id = models.IntegerField(null = True)
    original_title = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    date_published = models.DateField(null=True)
    genre = models.CharField(max_length=100, null=True)
    duration = models.IntegerField(null=True)
    language = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'movies_table'

    
