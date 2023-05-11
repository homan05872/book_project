# Generated by Django 4.2 on 2023-05-10 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0005_alter_book_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='book',
            name='bookname',
            field=models.CharField(max_length=100, verbose_name='書籍名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('bussines', 'ビジネス'), ('life', '生活'), ('novel', '小説'), ('comic', 'マンガ'), ('other', 'その他')], max_length=100, verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookuser', to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bookカバー'),
        ),
        migrations.AlterField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿日'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='ニックネーム'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='outher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiels', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='text',
            field=models.TextField(verbose_name='自己紹介'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='book.book', verbose_name='本'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewuser', to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='評価'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿日'),
        ),
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
        migrations.AlterModelTable(
            name='profiel',
            table='profiels',
        ),
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
    ]