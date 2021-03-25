from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TambahProduk(models.Model):
    title = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=9, decimal_places=3)
    img_produk = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title


class Produk(models.Model):
    title = models.CharField(max_length=100)
    deskripsi = models.TextField()
    time_upload = models.DateField(auto_now_add=True)
    img = models.ImageField(
        upload_to='img')
    publish = models.BooleanField()

    def __str__(self):
        return self.title


class Testimoni(models.Model):
    title = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    text = models.TextField()
    jabatan = models.TextField(max_length=50)

    def __str__(self):
        return self.title


class KataMereka(models.Model):
    title = models.CharField(max_length=100)
    img_mereka = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title


class Video(models.Model):
    caption = models.CharField(max_length=50)
    video = models.FileField(upload_to='video')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'video'

    def __str__(self):
        return self.caption
