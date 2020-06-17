#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

#['Enlem(N)', 'Boylam(E)', 'Derinlik(km)', 'ML', 'Yer', 'Çözüm']

class SonDepremler(models.Model):
    TarihveSaat = models.CharField(unique=True,max_length=100,error_messages=None) #unique=True
    Derinlik = models.CharField(max_length=100)
    Buyukluk = models.CharField(max_length=100)
    Mekan = models.CharField(max_length=100)
    Sene = models.IntegerField()
    Ay = models.IntegerField()
    Gün = models.IntegerField()
    Saat = models.IntegerField()
    Dakika = models.IntegerField()
    geom = models.PointField()

    def __str__(self):
        return self.TarihveSaat


    class Meta:
        verbose_name_plural = 'SonDepremler'

