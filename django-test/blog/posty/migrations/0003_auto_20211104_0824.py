# Generated by Django 2.2 on 2021-11-04 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0002_auto_20211104_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_dodania',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
