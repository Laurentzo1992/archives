# Generated by Django 4.2.2 on 2023-06-19 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fond", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sous_sous_serie",
            old_name="Serie",
            new_name="soussousserie",
        ),
    ]