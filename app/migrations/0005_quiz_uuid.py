# Generated by Django 3.2.7 on 2021-09-21 14:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_option_answer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
