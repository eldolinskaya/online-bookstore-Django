# Generated by Django 2.2.5 on 2019-09-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190930_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='quantity_for_sale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
    ]
