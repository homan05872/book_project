# Generated by Django 4.2 on 2023-05-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_review_title_alter_book_bookname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiel',
            name='sex',
            field=models.CharField(choices=[('男性', '男性'), ('女性', '女性')], max_length=50, verbose_name='性別'),
        ),
    ]
