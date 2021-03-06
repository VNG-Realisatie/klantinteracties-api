# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## Medewerker

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/medewerker)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| identificatie | Een korte unieke aanduiding van de MEDEWERKER. | string | nee | C​R​U​D |
| achternaam | De achternaam zoals de MEDEWERKER die in het dagelijkse verkeer gebruikt. | string | nee | C​R​U​D |
| voorletters | De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen. | string | nee | C​R​U​D |
| voorvoegselAchternaam | Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), voorvoegseltabel, en door een spatie van de geslachtsnaam is | string | nee | C​R​U​D |

## ContactMoment

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/contactmoment)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| bronorganisatie | Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de klantinteractie heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef | string | ja | C​R​U​D |
| klant | URL-referentie naar een KLANT indien de klantinteractie niet anoniem is. | string | nee | C​R​U​D |
| interactiedatum | De datum en het tijdstip waarop de klantinteractie heeft plaatsgevonden. | string | nee | C​R​U​D |
| kanaal | Het communicatiekanaal waarlangs het CONTACTMOMENT gevoerd wordt | string | nee | C​R​U​D |
| voorkeurskanaal | Het communicatiekanaal dat voor opvolging van de klantinteractie de voorkeur heeft van de KLANT. | string | nee | C​R​U​D |
| tekst | Een toelichting die inhoudelijk de klantinteractie van de klant beschrijft. | string | nee | C​R​U​D |
| onderwerpLinks | Eén of meerdere links naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden op onderwerp. | array | nee | C​R​U​D |
| initiatiefnemer | De partij die het contact heeft geïnitieerd. | string | nee | C​R​U​D |
| medewerker | URL-referentie naar een medewerker | string | nee | C​R​U​D |

## Klant

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/klant)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| voornaam | De voornaam, voorletters of roepnaam van de klant. | string | nee | C​R​U​D |
| achternaam | De achternaam van de klant. | string | nee | C​R​U​D |
| adres | Het adres van de klant. | string | nee | C​R​U​D |
| telefoonnummer | Het mobiele of vaste telefoonnummer van de klant. | string | nee | C​R​U​D |
| emailadres | Het e-mail adres van de klant. | string | nee | C​R​U​D |
| functie | De functie van de klant. | string | nee | C​R​U​D |
| subject | URL-referentie naar een subject | string | nee | C​R​U​D |
| subjectType | Type van de `subject`.

Uitleg bij mogelijke waarden:

* `natuurlijk_persoon` - Natuurlijk persoon
* `niet_natuurlijk_persoon` - Niet-natuurlijk persoon
* `vestiging` - Vestiging | string | nee | C​R​U​D |

## SubVerblijfBuitenland

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/subverblijfbuitenland)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| lndLandcode | De code, behorende bij de landnaam, zoals opgenomen in de Land/Gebied-tabel van de BRP. | string | ja | C​R​U​D |
| lndLandnaam | De naam van het land, zoals opgenomen in de Land/Gebied-tabel van de BRP. | string | ja | C​R​U​D |
| subAdresBuitenland1 |  | string | nee | C​R​U​D |
| subAdresBuitenland2 |  | string | nee | C​R​U​D |
| subAdresBuitenland3 |  | string | nee | C​R​U​D |

## NatuurlijkPersoon

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/natuurlijkpersoon)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| inpBsn | Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. | string | nee | C​R​U​D |
| anpIdentificatie | Het door de gemeente uitgegeven unieke nummer voor een ANDER NATUURLIJK PERSOON | string | nee | C​R​U​D |
| inpANummer | Het administratienummer van de persoon, bedoeld in de Wet BRP | string | nee | C​R​U​D |
| geslachtsnaam | De stam van de geslachtsnaam. | string | nee | C​R​U​D |
| voorvoegselGeslachtsnaam |  | string | nee | C​R​U​D |
| voorletters | De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen. | string | nee | C​R​U​D |
| voornamen | Voornamen bij de naam die de persoon wenst te voeren. | string | nee | C​R​U​D |
| geslachtsaanduiding | Een aanduiding die aangeeft of de persoon een man of een vrouw is, of dat het geslacht nog onbekend is.

Uitleg bij mogelijke waarden:

* `m` - Man
* `v` - Vrouw
* `o` - Onbekend | string | nee | C​R​U​D |
| geboortedatum |  | string | nee | C​R​U​D |

## NietNatuurlijkPersoon

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/nietnatuurlijkpersoon)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| innNnpId | Het door een kamer toegekend uniek nummer voor de INGESCHREVEN NIET-NATUURLIJK PERSOON | string | nee | C​R​U​D |
| annIdentificatie | Het door de gemeente uitgegeven unieke nummer voor een ANDER NIET-NATUURLIJK PERSOON | string | nee | C​R​U​D |
| statutaireNaam | Naam van de niet-natuurlijke persoon zoals deze is vastgelegd in de statuten (rechtspersoon) of in de vennootschapsovereenkomst is overeengekomen (Vennootschap onder firma of Commanditaire vennootschap). | string | nee | C​R​U​D |
| innRechtsvorm | De juridische vorm van de NIET-NATUURLIJK PERSOON. | string | nee | C​R​U​D |
| bezoekadres | De gegevens over het adres van de NIET-NATUURLIJK PERSOON | string | nee | C​R​U​D |

## Vestiging

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/vestiging)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| vestigingsNummer | Een korte unieke aanduiding van de Vestiging. | string | nee | C​R​U​D |
| handelsnaam | De naam van de vestiging waaronder gehandeld wordt. | array | nee | C​R​U​D |

## ObjectContactMoment

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/objectcontactmoment)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| contactmoment | URL-referentie naar het CONTACTMOMENT. | string | ja | C​R​U​D |
| object | URL-referentie naar het gerelateerde OBJECT (in een andere API). | string | ja | C​R​U​D |
| objectType | Het type van het gerelateerde OBJECT.

Uitleg bij mogelijke waarden:

* `zaak` - Zaak | string | ja | C​R​U​D |

## ObjectVerzoek

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/objectverzoek)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| verzoek | URL-referentie naar het VERZOEK. | string | ja | C​R​U​D |
| object | URL-referentie naar het gerelateerde OBJECT (in een andere API). | string | ja | C​R​U​D |
| objectType | Het type van het gerelateerde OBJECT.

Uitleg bij mogelijke waarden:

* `zaak` - Zaak | string | ja | C​R​U​D |

## VerzoekContactMoment

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/verzoekcontactmoment)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| contactmoment | URL-referentie naar het CONTACTMOMENT. | string | ja | C​R​U​D |
| verzoek | URL-referentie naar het VERZOEK. | string | ja | C​R​U​D |

## Verzoek

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/verzoek)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| identificatie | De unieke identificatie van het VERZOEK binnen de organisatie die verantwoordelijk is voor de behandeling van het VERZOEK. | string | nee | C​R​U​D |
| bronorganisatie | Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de klantinteractie heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef | string | ja | C​R​U​D |
| externeIdentificatie | De identificatie van het VERZOEK buiten de eigen organisatie. | string | nee | C​R​U​D |
| klant | URL-referentie naar een KLANT indien de klantinteractie niet anoniem is. | string | nee | C​R​U​D |
| interactiedatum | De datum en het tijdstip waarop de klantinteractie heeft plaatsgevonden. | string | nee | C​R​U​D |
| voorkeurskanaal | Het communicatiekanaal dat voor opvolging van de klantinteractie de voorkeur heeft van de KLANT. | string | nee | C​R​U​D |
| tekst | Een toelichting die inhoudelijk de klantinteractie van de klant beschrijft. | string | nee | C​R​U​D |
| status | De waarden van de typering van de voortgang van afhandeling van een VERZOEK.

Uitleg bij mogelijke waarden:

* `ontvangen` - (Ontvangen) Het verzoek is ingediend en door de organisatie ontvangen.
* `in_behandeling` - (In behandeling) Het is verzoek is in behandeling.
* `afgehandeld` - (Afgehandeld) Het verzoek zelf is afgehandeld. Eventuele vervolg acties, zoals zaken die voortkomen uit het verzoek, hebben een eigen status.
* `afgewezen` - (Afgewezen) Het verzoek is afgewezen zonder vervolg acties.
* `ingetrokken` - (Ingetrokken) De indiener heeft het verzoek ingetrokken. | string | ja | C​R​U​D |

## VerzoekInformatieObject

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/verzoekinformatieobject)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| informatieobject | URL-referentie naar het INFORMATIEOBJECT (in de Documenten API) waarin (een deel van) het verzoek beschreven is of aanvullende informatie biedt bij het VERZOEK. | string | ja | C​R​U​D |
| verzoek | URL-referentie naar het VERZOEK. | string | ja | C​R​U​D |

## VerzoekProduct

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/verzoekproduct)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| verzoek | URL-referentie naar het VERZOEK. | string | ja | C​R​U​D |
| product | URL-referentie naar het PRODUCT (in de Producten en Diensten API). | string | nee | C​R​U​D |


* Create, Read, Update, Delete
