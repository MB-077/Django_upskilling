# Generated by Django 5.0.6 on 2024-06-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
