# Generated by Django 5.0.6 on 2024-06-14 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 14, 8, 56, 49, 979627, tzinfo=datetime.timezone.utc)),
        ),
    ]
