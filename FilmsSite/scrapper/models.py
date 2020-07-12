from django.db import models


# Create your models here.
class Film(models.Model):
    film_id = models.IntegerField(null=False, unique=True, serialize=True)
    title = models.CharField(max_length=50, null=False)
    genre = models.CharField(max_length=40)
    premier = models.DateTimeField(max_length=4)  # todo выставить правильный формат
    avg_tomatometer = models.CharField(max_length=3)  # Persange
    avg_audience_score = models.CharField(max_length=3)  # Persange

    def __str__(self):
        return f'{self.title} tomatometer: {self.avg_tomatometer}, audience: {self.avg_audience_score}'

    # ф-ция для inserta в БД
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
