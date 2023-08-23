# Generated by Django 4.2.3 on 2023-08-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('visit_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='published_year',
            new_name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published',
        ),
    ]
