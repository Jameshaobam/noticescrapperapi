from rest_framework import serializers


class NoticeSerializer(serializers.Serializer):
    head = serializers.CharField(max_length=200)
    url = serializers.URLField(max_length=700)
    is_new_notice = serializers.BooleanField(default=False)
