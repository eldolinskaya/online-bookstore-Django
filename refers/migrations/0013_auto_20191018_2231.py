# Generated by Django 2.2.5 on 2019-10-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refers', '0012_auto_20191018_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='typecover',
            name='descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
    ]