from django.shortcuts import render
from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_GEO_DISTANCE
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (FilteringFilterBackend, OrderingFilterBackend,
                                                          SearchFilterBackend, DefaultOrderingFilterBackend)
from elastic.document import PublisherDocument
from elastic.serializer import PublisherDocumentSerializer



class PublisherDocumentView(DocumentViewSet):
    document = PublisherDocument
    serializer_class = PublisherDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    search_field = ('name',
                    'info',
                    'address',
                    'city',
                    'state_province',
                    'country',)
    multi_match_search_fields = ('title', 'content')
    fields_fields = {
        'id': None,
        'name': 'name.raw',
        'city': 'city.raw',
        'state_province': 'state_province.raw',
        'country': 'country.raw',
    }
    ordering_fields = {
        'id': None,
        'name': None,
        'city': None,
        'country': None,
    }
    ordering = ('id', 'name',)

    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }

