# Generated by Django 2.2.5 on 2019-09-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=1900),
            preserve_default=False,
        ),
    ]
