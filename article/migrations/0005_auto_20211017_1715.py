# Generated by Django 3.1.3 on 2021-10-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20211017_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='written_time',
            field=models.DateField(),
        ),
    ]