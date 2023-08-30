# Generated by Django 3.1.8 on 2023-08-30 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_auto_20230830_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
