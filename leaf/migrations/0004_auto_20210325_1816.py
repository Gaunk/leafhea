# Generated by Django 3.1.7 on 2021-03-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0003_tambahmember_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tambahmember',
            name='kategori',
            field=models.CharField(choices=[('Leader', 'Member')], max_length=200, null=True),
        ),
    ]
