# Generated by Django 4.2.4 on 2023-08-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=130),
        ),
    ]
