# Generated by Django 3.2.7 on 2021-09-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_quiz_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='slug',
        ),
    ]
