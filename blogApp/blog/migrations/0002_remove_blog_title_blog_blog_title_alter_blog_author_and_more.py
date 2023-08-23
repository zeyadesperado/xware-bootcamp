# Generated by Django 4.2.3 on 2023-08-10 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(default='Untitled', max_length=70),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_text',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
