# Generated by Django 3.2.3 on 2021-06-20 22:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 22, 37, 0, 342864, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
