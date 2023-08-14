# Generated by Django 4.2.4 on 2023-08-12 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Showroom", "0003_alter_model_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model",
            name="brand",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="Showroom.brand",
            ),
        ),
    ]