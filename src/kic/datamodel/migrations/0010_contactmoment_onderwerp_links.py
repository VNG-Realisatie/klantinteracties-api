# Generated by Django 2.2.6 on 2019-11-25 15:38

from django.db import migrations, models

import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0009_verzoekinformatieobject"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactmoment",
            name="onderwerp_links",
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.URLField(
                    help_text="URL naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden.",
                    max_length=1000,
                    verbose_name="onderwerp link",
                ),
                blank=True,
                default=list,
                help_text="Eén of meerdere links naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden op onderwerp.",
                size=None,
            ),
        ),
    ]
