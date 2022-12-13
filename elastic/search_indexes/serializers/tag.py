from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    title =serializers.CharField()

    class Meta:
        fields = ('title',)
        read_only_fields = ('title',)