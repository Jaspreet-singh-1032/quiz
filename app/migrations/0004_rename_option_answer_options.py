# Generated by Django 3.2.7 on 2021-09-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='option',
            new_name='options',
        ),
    ]
