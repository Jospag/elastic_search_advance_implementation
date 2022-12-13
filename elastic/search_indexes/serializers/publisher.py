from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class PublisherDocumentSerializer(DocumentSerializer):
    """Serializer for Publisher document."""

    class Meta:

        fields = (
            'id',
            'name',
            'info',
            'address',
            'city',
            'state',
            'country',
        )