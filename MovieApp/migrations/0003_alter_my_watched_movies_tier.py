# Generated by Django 5.0.1 on 2024-03-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_watched_movies',
            name='tier',
            field=models.TextField(default='F', null=True),
        ),
    ]
