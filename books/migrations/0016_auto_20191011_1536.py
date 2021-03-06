# Generated by Django 2.2.5 on 2019-10-11 12:36

import books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_journal_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='age_restrictions',
            field=models.CharField(max_length=50, verbose_name='Возрастные ограничения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refers.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно к заказу'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_ISBN',
            field=models.CharField(max_length=50, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_format',
            field=models.CharField(max_length=50, verbose_name='Формат'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=books.models.image_folder, verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refers.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.IntegerField(verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, BYN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity_for_sale',
            field=models.IntegerField(verbose_name='Количество книг в наличии'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refers.Serie', verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type_cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refers.TypeCover', verbose_name='Переплёт'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight_gram',
            field=models.IntegerField(verbose_name='Вес, гр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно к заказу'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='month',
            field=models.CharField(max_length=50, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='number',
            field=models.IntegerField(verbose_name='Выпуск'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='page',
            field=models.IntegerField(verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, BYN'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
    ]
