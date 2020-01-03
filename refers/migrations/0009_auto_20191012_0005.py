# Generated by Django 2.2.5 on 2019-10-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refers', '0008_auto_20191011_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(help_text='Введите ФИО автора', max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Введите наименование жанра', max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='name',
            field=models.CharField(help_text='Введите название издательства', max_length=200, verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(help_text='Введите наименование серии', max_length=100, verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='typecover',
            name='name',
            field=models.CharField(help_text='Введите вид переплёта', max_length=50, verbose_name='Переплёт'),
        ),
    ]