# Generated by Django 3.1.3 on 2021-10-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20211020_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_content',
            field=models.TextField(null=True),
        ),
    ]
