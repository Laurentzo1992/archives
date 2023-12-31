# Generated by Django 4.2.2 on 2023-06-30 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cote", "0001_initial"),
        ("fond", "0001_initial"),
        ("paramettre", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Descripteur",
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
                (
                    "descripteur",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="DescripteurArchive",
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
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Fichier",
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
                (
                    "fichier",
                    models.FileField(blank=True, null=True, upload_to="archives"),
                ),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="FichierArchive",
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
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tache",
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
                ("analyse", models.TextField()),
                ("date_extrem", models.DateField()),
                ("doc_manquant", models.TextField()),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                ("modified_at", models.DateTimeField(auto_now_add=True)),
                (
                    "boite",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cote.boite",
                    ),
                ),
                (
                    "descripteur",
                    models.ManyToManyField(
                        through="gestion.DescripteurArchive", to="gestion.descripteur"
                    ),
                ),
                (
                    "fichier",
                    models.ManyToManyField(
                        through="gestion.FichierArchive", to="gestion.fichier"
                    ),
                ),
                (
                    "provenance",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paramettre.provenance",
                    ),
                ),
                (
                    "rayon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cote.rayon",
                    ),
                ),
                (
                    "salle",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cote.salle",
                    ),
                ),
                (
                    "serie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fond.serie",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cote.site",
                    ),
                ),
                (
                    "sous_serie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fond.sous_serie",
                    ),
                ),
                (
                    "sous_sous_serie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fond.sous_sous_serie",
                    ),
                ),
                (
                    "status_archive",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paramettre.archive_statuts",
                    ),
                ),
                (
                    "travee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cote.travee",
                    ),
                ),
                (
                    "type_archive",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paramettre.archive_type",
                    ),
                ),
                (
                    "type_doc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paramettre.document_type",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="fichierarchive",
            name="archive",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gestion.tache",
            ),
        ),
        migrations.AddField(
            model_name="fichierarchive",
            name="fichier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gestion.fichier",
            ),
        ),
        migrations.AddField(
            model_name="descripteurarchive",
            name="archive",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gestion.tache",
            ),
        ),
        migrations.AddField(
            model_name="descripteurarchive",
            name="descripteur",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gestion.descripteur",
            ),
        ),
    ]
