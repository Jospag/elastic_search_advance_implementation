from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from elastic.models import Publisher
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_GEO_DISTANCE,
)

PUBLISHER_INDEX = Index('Publisher')

PUBLISHER_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas = 1
)

@PUBLISHER_INDEX.doc_type
class PublisherDocument(Document):
    id = fields.IntegerField(attr='id')
    name = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    info = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    address = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    city = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    state_province = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    country = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    class Django(object):
        model = Publisher