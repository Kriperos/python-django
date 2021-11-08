from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor_imie = models.CharField(max_length=30)
    autor_nazwisko = models.CharField(max_length=30)
    data_dodania = models.DateTimeField(default=timezone.now)
    tresc = models.TextField()

    def __str__(self):
        return f"{self.autor_imie} {self.autor_nazwisko} {self.data_dodania:%Y-%m-%d %H:%M:%S}, id: {self.pk}"
