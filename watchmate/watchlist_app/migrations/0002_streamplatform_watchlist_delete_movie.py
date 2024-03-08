# Generated by Django 5.0.2 on 2024-03-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StreamPlatform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("about", models.CharField(max_length=150)),
                ("website", models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="WatchList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
    ]