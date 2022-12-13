# from django_elasticsearch_dsl_drf import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers


class PublisherDocumentSerializer(DocumentSerializer):
    location = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'name',
            'info',
            'address',
            'city',
            'state_province',
            'country',
        )

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
