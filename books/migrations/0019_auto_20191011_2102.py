# Generated by Django 2.2.5 on 2019-10-11 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20191011_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refers.PublishingHouse', verbose_name='Издательство'),
        ),
    ]
