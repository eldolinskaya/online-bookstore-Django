# Generated by Django 2.2.5 on 2019-11-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191015_2259'),
        ('order', '0006_order_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Profile', verbose_name='Личные данные'),
        ),
    ]