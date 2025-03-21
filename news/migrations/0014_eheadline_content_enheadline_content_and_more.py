# Generated by Django 5.0.4 on 2025-03-16 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0013_alter_eheadline_id_alter_enheadline_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="eheadline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="enheadline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="headline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="lheadline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pheadline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sheadline",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("image", models.URLField()),
                ("content", models.TextField(blank=True, null=True)),
                ("source", models.CharField(max_length=255)),
                (
                    "dislikes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="disliked_articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "favorites",
                    models.ManyToManyField(
                        blank=True,
                        related_name="favorite_articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
