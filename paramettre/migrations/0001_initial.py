# Generated by Django 4.2.2 on 2023-06-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive_statuts",
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
                ("libelle", models.CharField(blank=True, max_length=200, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Archive_type",
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
                ("libelle", models.CharField(blank=True, max_length=200, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Document_type",
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
                ("libelle", models.CharField(blank=True, max_length=200, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Provenance",
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
                ("sigle", models.CharField(blank=True, max_length=50, null=True)),
                ("nom", models.CharField(blank=True, max_length=200, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
