from django.conf import settings
from django_elasticsearch_dsl import Index, Document, fields

from elastic.models.publisher import Publisher

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@INDEX.doc_type
class PublisherDocument(Document):
    id = fields.IntegerField(attr='id')
    name = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    info = fields.TextField()
    address = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    city = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    state = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    country = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )

    class Meta:
        model = Publisher