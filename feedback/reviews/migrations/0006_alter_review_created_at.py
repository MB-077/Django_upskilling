# Generated by Django 5.0.6 on 2024-06-17 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 17, 14, 3, 38, 962389)),
        ),
    ]