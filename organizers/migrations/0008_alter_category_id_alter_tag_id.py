# Generated by Django 5.2.4 on 2025-07-20 15:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0007_alter_category_id_alter_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
