# Generated by Django 2.2.5 on 2019-11-08 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20191016_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тэги для поиска'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='refers.Author', verbose_name='Автор'),
        ),
    ]
