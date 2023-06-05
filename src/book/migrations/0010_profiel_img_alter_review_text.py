# Generated by Django 4.2 on 2023-06-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_book_profiel_connect'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=500, verbose_name='本文'),
        ),
    ]
