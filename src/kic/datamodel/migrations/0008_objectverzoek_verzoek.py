# Generated by Django 2.2.6 on 2019-11-18 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid
import vng_api_common.models


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0007_auto_20191114_1142"),
    ]

    operations = [
        migrations.CreateModel(
            name="Verzoek",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unieke resource identifier (UUID4)",
                        unique=True,
                    ),
                ),
                (
                    "datumtijd",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="De datum en het tijdstip waarop het CONTACTMOMENT begint",
                    ),
                ),
                (
                    "tekst",
                    models.TextField(
                        blank=True,
                        help_text="Een toelichting die inhoudelijk het contact met de klant beschrijft.",
                    ),
                ),
                (
                    "klant",
                    models.ForeignKey(
                        blank=True,
                        help_text="URL-referentie naar een KLANT (in de Contactmomenten API) indien het contactmoment niet anoniem is.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.Klant",
                    ),
                ),
            ],
            options={"verbose_name": "verzoek", "verbose_name_plural": "verzoeken",},
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
        migrations.CreateModel(
            name="ObjectVerzoek",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unieke resource identifier (UUID4)",
                        unique=True,
                    ),
                ),
                (
                    "object",
                    models.URLField(
                        help_text="URL-referentie naar het gerelateerde OBJECT (in een andere API)."
                    ),
                ),
                (
                    "object_type",
                    models.CharField(
                        choices=[("zaak", "Zaak")],
                        help_text="Het type van het gerelateerde OBJECT.",
                        max_length=100,
                        verbose_name="objecttype",
                    ),
                ),
                (
                    "verzoek",
                    models.ForeignKey(
                        help_text="URL-referentie naar het VERZOEK.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.Verzoek",
                    ),
                ),
            ],
            options={
                "verbose_name": "object-verzoek",
                "verbose_name_plural": "object-verzoeken",
                "unique_together": {("verzoek", "object")},
            },
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
    ]
