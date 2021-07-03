# Generated by Django 3.0.8 on 2021-06-08 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_card_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='taskid',
            field=models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False, unique=True),
        ),
    ]
