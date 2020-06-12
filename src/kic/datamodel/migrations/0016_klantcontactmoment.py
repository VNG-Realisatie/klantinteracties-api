# Generated by Django 2.2.11 on 2020-06-12 09:37

from django.db import migrations, models
import django.db.models.deletion
import uuid
import vng_api_common.models


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0015_auto_20200320_1626"),
    ]

    operations = [
        migrations.CreateModel(
            name="KlantContactMoment",
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
                    "rol",
                    models.CharField(
                        choices=[
                            ("belanghebbende", "Belanghebbende"),
                            ("gesprekspartner", "Gesprekspartner"),
                        ],
                        help_text="De rol van de KLANT in het CONTACTMOMENT. Indien de KLANT zowel gesprekspartner als belanghebbende is, dan worden er twee KLANTCONTACTMOMENTen aangemaakt.",
                        max_length=15,
                    ),
                ),
                (
                    "contactmoment",
                    models.ForeignKey(
                        help_text="URL-referentie naar het CONTACTMOMENT.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.ContactMoment",
                    ),
                ),
                (
                    "klant",
                    models.ForeignKey(
                        help_text="URL-referentie naar de KLANT in het CONTACTMOMENT",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.Klant",
                    ),
                ),
            ],
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
    ]