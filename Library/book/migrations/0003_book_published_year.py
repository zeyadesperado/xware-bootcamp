# Generated by Django 4.2.3 on 2023-08-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]