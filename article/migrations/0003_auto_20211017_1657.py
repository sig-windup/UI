# Generated by Django 3.1.3 on 2021-10-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20211014_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='written_time',
            field=models.DateField(),
        ),
    ]
