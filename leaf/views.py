from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def home(request):
    produk = Produk.objects.all()
    testimoni = Testimoni.objects.all()
    tambah_produk = TambahProduk.objects.all()
    katamereka = KataMereka.objects.all()
    context = {
        'produk': produk,
        'testimoni': testimoni,
        'tambah_produk': tambah_produk,
        'katamereka': katamereka,
    }

    return render(request, 'base_code.html', context)
