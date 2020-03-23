# Generated by Django 2.2.11 on 2020-03-18 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0012_auto_20191218_1231"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactmoment",
            name="voorkeurskanaal",
            field=models.CharField(
                blank=True,
                help_text="Het communicatiekanaal dat voor opvolging van het CONTACTMOMENT de voorkeur heeft van de KLANT.",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="verzoek",
            name="voorkeurskanaal",
            field=models.CharField(
                blank=True,
                help_text="Het communicatiekanaal dat voor opvolging van het CONTACTMOMENT de voorkeur heeft van de KLANT.",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="contactmoment",
            name="interactiedatum",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="De datum en het tijdstip waarop het verzoek is ingediend.",
            ),
        ),
        migrations.AlterField(
            model_name="contactmoment",
            name="klant",
            field=models.ForeignKey(
                blank=True,
                help_text="URL-referentie naar een KLANT indien het verzoek niet anoniem is.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.Klant",
            ),
        ),
        migrations.AlterField(
            model_name="contactmoment",
            name="tekst",
            field=models.TextField(
                blank=True,
                help_text="Een toelichting die inhoudelijk het verzoek van de klant beschrijft.",
            ),
        ),
        migrations.AlterField(
            model_name="verzoek",
            name="interactiedatum",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="De datum en het tijdstip waarop het verzoek is ingediend.",
            ),
        ),
        migrations.AlterField(
            model_name="verzoek",
            name="klant",
            field=models.ForeignKey(
                blank=True,
                help_text="URL-referentie naar een KLANT indien het verzoek niet anoniem is.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.Klant",
            ),
        ),
        migrations.AlterField(
            model_name="verzoek",
            name="tekst",
            field=models.TextField(
                blank=True,
                help_text="Een toelichting die inhoudelijk het verzoek van de klant beschrijft.",
            ),
        ),
    ]