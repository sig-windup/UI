# Generated by Django 3.1.3 on 2021-10-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='written_time',
            field=models.DateTimeField(),
        ),
    ]