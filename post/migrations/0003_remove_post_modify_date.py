# Generated by Django 3.1.3 on 2021-09-30 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='modify_date',
        ),
    ]
