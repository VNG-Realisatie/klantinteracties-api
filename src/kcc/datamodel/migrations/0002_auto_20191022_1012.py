# Generated by Django 2.2 on 2019-10-22 10:12

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vng_api_common.fields


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="NatuurlijkPersoon",
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
                    "inp_bsn",
                    vng_api_common.fields.BSNField(
                        blank=True,
                        help_text="Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer.",
                        max_length=9,
                    ),
                ),
                (
                    "anp_identificatie",
                    models.CharField(
                        blank=True,
                        help_text="Het door de gemeente uitgegeven unieke nummer voor een ANDER NATUURLIJK PERSOON",
                        max_length=17,
                    ),
                ),
                (
                    "inp_a_nummer",
                    models.CharField(
                        blank=True,
                        help_text="Het administratienummer van de persoon, bedoeld in de Wet BRP",
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="a-nummer-incorrect-format",
                                message="inpA_nummer must consist of 10 digits",
                                regex="^[1-9][0-9]{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "geslachtsnaam",
                    models.CharField(
                        blank=True,
                        help_text="De stam van de geslachtsnaam.",
                        max_length=200,
                    ),
                ),
                (
                    "voorvoegsel_geslachtsnaam",
                    models.CharField(blank=True, max_length=80),
                ),
                (
                    "voorletters",
                    models.CharField(
                        blank=True,
                        help_text="De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen.",
                        max_length=20,
                    ),
                ),
                (
                    "voornamen",
                    models.CharField(
                        blank=True,
                        help_text="Voornamen bij de naam die de persoon wenst te voeren.",
                        max_length=200,
                    ),
                ),
                (
                    "geslachtsaanduiding",
                    models.CharField(
                        blank=True,
                        choices=[("m", "Man"), ("v", "Vrouw"), ("o", "Onbekend")],
                        help_text="Een aanduiding die aangeeft of de persoon een man of een vrouw is, of dat het geslacht nog onbekend is.",
                        max_length=1,
                    ),
                ),
                ("geboortedatum", models.CharField(blank=True, max_length=18)),
            ],
            options={"verbose_name": "natuurlijk persoon"},
        ),
        migrations.AddField(
            model_name="klant",
            name="betrokkene",
            field=models.URLField(
                blank=True,
                help_text="URL-referentie naar een betrokkene",
                max_length=1000,
            ),
        ),
        migrations.AddField(
            model_name="klant",
            name="betrokkene_type",
            field=models.CharField(
                choices=[
                    ("natuurlijk_persoon", "Natuurlijk persoon"),
                    ("vestiging", "Vestiging"),
                ],
                default="natuurlijk_persoon",
                help_text="Type van de `betrokkene`.",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Vestiging",
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
                    "vestigings_nummer",
                    models.CharField(
                        blank=True,
                        help_text="Een korte unieke aanduiding van de Vestiging.",
                        max_length=24,
                    ),
                ),
                (
                    "handelsnaam",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(blank=True, max_length=625),
                        default=list,
                        help_text="De naam van de vestiging waaronder gehandeld wordt.",
                        size=None,
                    ),
                ),
                (
                    "klant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.Klant",
                    ),
                ),
            ],
            options={"verbose_name": "vestiging"},
        ),
        migrations.CreateModel(
            name="SubVerblijfBuitenland",
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
                    "lnd_landcode",
                    models.CharField(
                        help_text="De code, behorende bij de landnaam, zoals opgenomen in de Land/Gebied-tabel van de BRP.",
                        max_length=4,
                    ),
                ),
                (
                    "lnd_landnaam",
                    models.CharField(
                        help_text="De naam van het land, zoals opgenomen in de Land/Gebied-tabel van de BRP.",
                        max_length=40,
                    ),
                ),
                ("sub_adres_buitenland_1", models.CharField(blank=True, max_length=35)),
                ("sub_adres_buitenland_2", models.CharField(blank=True, max_length=35)),
                ("sub_adres_buitenland_3", models.CharField(blank=True, max_length=35)),
                (
                    "natuurlijkpersoon",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_verblijf_buitenland",
                        to="datamodel.NatuurlijkPersoon",
                    ),
                ),
                (
                    "vestiging",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_verblijf_buitenland",
                        to="datamodel.Vestiging",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="natuurlijkpersoon",
            name="klant",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="natuurlijk_persoon",
                to="datamodel.Klant",
            ),
        ),
        migrations.CreateModel(
            name="Adres",
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
                    "aoa_identificatie",
                    models.CharField(
                        help_text="De unieke identificatie van het OBJECT",
                        max_length=100,
                    ),
                ),
                ("wpl_woonplaats_naam", models.CharField(max_length=80)),
                (
                    "gor_openbare_ruimte_naam",
                    models.CharField(
                        help_text="Een door het bevoegde gemeentelijke orgaan aan een OPENBARE RUIMTE toegekende benaming",
                        max_length=80,
                    ),
                ),
                (
                    "aoa_huisnummer",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(99999)]
                    ),
                ),
                ("aoa_huisletter", models.CharField(blank=True, max_length=1)),
                (
                    "aoa_huisnummertoevoeging",
                    models.CharField(blank=True, max_length=4),
                ),
                ("aoa_postcode", models.CharField(blank=True, max_length=7)),
                (
                    "inp_locatiebeschrijving",
                    models.CharField(blank=True, max_length=1000),
                ),
                (
                    "natuurlijkpersoon",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verblijfsadres",
                        to="datamodel.NatuurlijkPersoon",
                    ),
                ),
                (
                    "vestiging",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verblijfsadres",
                        to="datamodel.Vestiging",
                    ),
                ),
            ],
        ),
    ]
