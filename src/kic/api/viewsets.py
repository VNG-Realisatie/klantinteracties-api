import logging

from django.core.cache import caches

from rest_framework import mixins, viewsets
from rest_framework.serializers import ValidationError
from rest_framework.settings import api_settings
from vng_api_common.permissions import AuthScopesRequired
from vng_api_common.viewsets import CheckQueryParamsMixin

from kic.datamodel.models import (
    ContactMoment,
    Klant,
    ObjectContactMoment,
    VerzoekContactMoment,
    VerzoekInformatieObject,
    VerzoekProduct,
)
from kic.datamodel.models.core import ObjectVerzoek, Verzoek

from .filters import (
    ObjectContactMomentFilter,
    ObjectVerzoekFilter,
    VerzoekContactMomentFilter,
    VerzoekInformatieObjectFilter,
    VerzoekProductFilter,
)
from .scopes import (
    SCOPE_KLANTEN_AANMAKEN,
    SCOPE_KLANTEN_ALLES_LEZEN,
    SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    SCOPE_KLANTEN_BIJWERKEN,
)
from .serializers import (
    ContactMomentSerializer,
    KlantSerializer,
    ObjectContactMomentSerializer,
    ObjectVerzoekSerializer,
    VerzoekContactMomentSerializer,
    VerzoekInformatieObjectSerializer,
    VerzoekProductSerializer,
    VerzoekSerializer,
)
from .validators import (
    ObjectContactMomentDestroyValidator,
    ObjectVerzoekDestroyValidator,
)

logger = logging.getLogger(__name__)


class KlantViewSet(viewsets.ModelViewSet):
    """
    Opvragen en bewerken van KLANTen.

    Een KLANT is een eenvoudige weergave van een NATUURLIJK PERSOON of
    VESTIGING waarbij het gaat om niet geverifieerde gegevens. Om deze reden
    zijn ook alle attributen optioneel.

    Indien de KLANT geverifieerd is mag een relatie gelegd worden met een
    NATUURLIJK PERSOON of VESTIGING  middels het attribuut `subject` of, indien
    er geen API beschikbaar is voor deze objecten, middels
    `subjectIdentificatie`.

    create:
    Maak een KLANT aan.

    Maak een KLANT aan.

    list:
    Alle KLANTen opvragen.

    Alle KLANTen opvragen.

    retrieve:
    Een specifiek KLANT opvragen.

    Een specifiek KLANT opvragen.

    update:
    Werk een KLANT in zijn geheel bij.

    Werk een KLANT in zijn geheel bij.

    partial_update:
    Werk een KLANT deels bij.

    Werk een KLANT deels bij.

    destroy:
    Verwijder een KLANT.

    Verwijder een KLANT.
    """

    queryset = Klant.objects.all()
    serializer_class = KlantSerializer
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }


class ContactMomentViewSet(viewsets.ModelViewSet):
    """
    Opvragen en bewerken van CONTACTMOMENTen.

    create:
    Maak een CONTACTMOMENT aan.

    Maak een CONTACTMOMENT aan.

    list:
    Alle CONTACTMOMENTen opvragen.

    Alle CONTACTMOMENTen opvragen.

    retrieve:
    Een specifiek CONTACTMOMENT opvragen.

    Een specifiek CONTACTMOMENT opvragen.

    update:
    Werk een CONTACTMOMENT in zijn geheel bij.

    Werk een CONTACTMOMENT in zijn geheel bij.

    partial_update:
    Werk een CONTACTMOMENT deels bij.

    Werk een CONTACTMOMENT deels bij.

    destroy:
    Verwijder een CONTACTMOMENT.

    Verwijder een CONTACTMOMENT.
    """

    queryset = ContactMoment.objects.all()
    serializer_class = ContactMomentSerializer
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }


class VerzoekViewSet(viewsets.ModelViewSet):
    """
    Opvragen en bewerken van VERZOEKen.

    create:
    Maak een VERZOEK aan.

    Maak een VERZOEK aan.

    list:
    Alle VERZOEKen opvragen.

    Alle VERZOEKen opvragen.

    retrieve:
    Een specifiek VERZOEK opvragen.

    Een specifiek VERZOEK opvragen.

    update:
    Werk een VERZOEK in zijn geheel bij.

    Werk een VERZOEK in zijn geheel bij.

    partial_update:
    Werk een VERZOEK deels bij.

    Werk een VERZOEK deels bij.

    destroy:
    Verwijder een VERZOEK.

    Verwijder een VERZOEK.
    """

    queryset = Verzoek.objects.all()
    serializer_class = VerzoekSerializer
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }


class ObjectContactMomentViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en verwijderen van OBJECT-CONTACTMOMENT relaties.

    Het betreft een relatie tussen een willekeurig OBJECT, bijvoorbeeld een
    ZAAK in de Zaken API, en een CONTACTMOMENT.

    create:
    Maak een OBJECT-CONTACTMOMENT relatie aan.

    Maak een OBJECT-CONTACTMOMENT relatie aan.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.

    list:
    Alle OBJECT-CONTACTMOMENT relaties opvragen.

    Alle OBJECT-CONTACTMOMENT relaties opvragen.

    retrieve:
    Een specifiek OBJECT-CONTACTMOMENT relatie opvragen.

    Een specifiek OBJECT-CONTACTMOMENT relatie opvragen.

    destroy:
    Verwijder een OBJECT-CONTACTMOMENT relatie.

    Verwijder een OBJECT-CONTACTMOMENT relatie.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.
    """

    queryset = ObjectContactMoment.objects.all()
    serializer_class = ObjectContactMomentSerializer
    filterset_class = ObjectContactMomentFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }

    def perform_destroy(self, instance):
        # destroy is only allowed if the remote relation does no longer exist, so check for that
        validator = ObjectContactMomentDestroyValidator()

        try:
            validator(instance)
        except ValidationError as exc:
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: exc}, code=exc.detail[0].code
            )
        else:
            super().perform_destroy(instance)


class ObjectVerzoekViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en verwijderen van OBJECT-VERZOEK relaties.

    Het betreft een relatie tussen een willekeurig OBJECT, bijvoorbeeld een
    ZAAK in de Zaken API, en een VERZOEK.

    create:
    Maak een OBJECT-VERZOEK relatie aan.

    Maak een OBJECT-VERZOEK relatie aan.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.

    list:
    Alle OBJECT-VERZOEK relaties opvragen.

    Alle OBJECT-VERZOEK relaties opvragen.

    retrieve:
    Een specifiek OBJECT-VERZOEK relatie opvragen.

    Een specifiek OBJECT-VERZOEK relatie opvragen.

    destroy:
    Verwijder een OBJECT-VERZOEK relatie.

    Verwijder een OBJECT-VERZOEK relatie.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.
    """

    queryset = ObjectVerzoek.objects.all()
    serializer_class = ObjectVerzoekSerializer
    filterset_class = ObjectVerzoekFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }

    def perform_destroy(self, instance):
        # destroy is only allowed if the remote relation does no longer exist, so check for that
        validator = ObjectVerzoekDestroyValidator()

        try:
            validator(instance)
        except ValidationError as exc:
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: exc}, code=exc.detail[0].code
            )
        else:
            super().perform_destroy(instance)


class VerzoekInformatieObjectViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en bewerken van VERZOEK-INFORMATIEOBJECT relaties.

    create:
    Maak een VERZOEK-INFORMATIEOBJECT relatie aan.

    Registreer een INFORMATIEOBJECT bij een VERZOEK. Er worden twee types van
    relaties met andere objecten gerealiseerd:

    **Er wordt gevalideerd op**
    - geldigheid `verzoek` URL
    - geldigheid `informatieobject` URL
    - de combinatie `informatieobject` en `verzoek` moet uniek zijn

    **Opmerkingen**
    - Bij het aanmaken wordt ook in de Documenten API de gespiegelde relatie
      aangemaakt, echter zonder de relatie-informatie.

    list:
    Alle VERZOEK-INFORMATIEOBJECT relaties opvragen.

    Deze lijst kan gefilterd wordt met query-string parameters.

    retrieve:
    Een specifieke VERZOEK-INFORMATIEOBJECT relatie opvragen.

    Een specifieke VERZOEK-INFORMATIEOBJECT relatie opvragen.

    update:
    Werk een VERZOEK-INFORMATIEOBJECT relatie in zijn geheel bij.

    Je mag enkel de gegevens van de relatie bewerken, en niet de relatie zelf
    aanpassen.

    **Er wordt gevalideerd op**
    - `informatieobject` URL en `verzoek` URL mogen niet veranderen

    partial_update:
    Werk een VERZOEK-INFORMATIEOBJECT relatie deels bij.

    Je mag enkel de gegevens van de relatie bewerken, en niet de relatie zelf
    aanpassen.

    **Er wordt gevalideerd op**
    - `informatieobject` URL en `verzoek` URL mogen niet veranderen

    destroy:
    Verwijder een VERZOEK-INFORMATIEOBJECT relatie.

    Verwijder een VERZOEK-INFORMATIEOBJECT relatie.
    """

    queryset = VerzoekInformatieObject.objects.all()
    serializer_class = VerzoekInformatieObjectSerializer
    filterset_class = VerzoekInformatieObjectFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
    }

    def get_queryset(self):
        qs = super().get_queryset()

        # Do not display BesluitInformatieObjecten that are marked to be deleted
        cache = caches["drc_sync"]

        # TODO: Store cachekeys somewhere central.
        marked_vios = cache.get("vios_marked_for_delete")
        if marked_vios:
            return qs.exclude(uuid__in=marked_vios)
        return qs


class VerzoekContactMomentViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en bewerken van VERZOEK-CONTACTMOMENT relaties.

    create:
    Maak een VERZOEK-CONTACTMOMENT relatie aan.

    Registreer een CONTACTMOMENT bij een VERZOEK. Er worden twee types van
    relaties met andere objecten gerealiseerd:

    **Er wordt gevalideerd op**
    - geldigheid `verzoek` URL
    - geldigheid `contactmoment` URL
    - de combinatie `contactmoment` en `verzoek` moet uniek zijn

    list:
    Alle VERZOEK-CONTACTMOMENT relaties opvragen.

    Deze lijst kan gefilterd wordt met query-string parameters.

    retrieve:
    Een specifieke VERZOEK-CONTACTMOMENT relatie opvragen.

    Een specifieke VERZOEK-CONTACTMOMENT relatie opvragen.

    update:
    Werk een VERZOEK-CONTACTMOMENT relatie in zijn geheel bij.

    Je mag enkel de gegevens van de relatie bewerken, en niet de relatie zelf
    aanpassen.

    **Er wordt gevalideerd op**
    - `contactmoment` URL en `verzoek` URL mogen niet veranderen

    partial_update:
    Werk een VERZOEK-CONTACTMOMENT relatie deels bij.

    Je mag enkel de gegevens van de relatie bewerken, en niet de relatie zelf
    aanpassen.

    **Er wordt gevalideerd op**
    - `contactmoment` URL en `verzoek` URL mogen niet veranderen

    destroy:
    Verwijder een VERZOEK-CONTACTMOMENT relatie.

    Verwijder een VERZOEK-CONTACTMOMENT relatie.
    """

    queryset = VerzoekContactMoment.objects.all()
    serializer_class = VerzoekContactMomentSerializer
    filterset_class = VerzoekContactMomentFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
    }


class VerzoekProductViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en bewerken van VERZOEK-PRODUCT relaties.

    create:
    Maak een VERZOEK-PRODUCT relatie aan.

    Registreer een PRODUCT bij een VERZOEK. Er worden twee types van
    relaties met andere objecten gerealiseerd:

    **Er wordt gevalideerd op**
    - geldigheid `verzoek` URL
    - geldigheid `product` URL

    list:
    Alle VERZOEK-PRODUCT relaties opvragen.

    Deze lijst kan gefilterd wordt met query-string parameters.

    retrieve:
    Een specifieke VERZOEK-PRODUCT relatie opvragen.

    Een specifieke VERZOEK-PRODUCT relatie opvragen.

    destroy:
    Verwijder een VERZOEK-PRODUCT relatie.

    Verwijder een VERZOEK-PRODUCT relatie.
    """

    queryset = VerzoekProduct.objects.all()
    serializer_class = VerzoekProductSerializer
    filterset_class = VerzoekProductFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
    }
