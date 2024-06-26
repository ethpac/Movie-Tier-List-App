# Generated by Django 5.0.1 on 2024-02-28 21:52

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField()),
                ('genre_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.TextField()),
                ('release_date', models.DateField(null=True)),
                ('title', models.TextField(verbose_name='Movie Name')),
                ('video', models.BooleanField()),
                ('vote_average', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='My_Watched_Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.TextField(default='')),
                ('tier', models.TextField(default='N', null=True)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.popular_movies')),
            ],
        ),
    ]
