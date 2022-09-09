from rest_framework import serializers
from extranotice.models import ExtraNotice

class NoticeSerializer(serializers.Serializer):
    head = serializers.CharField(max_length=200)
    url = serializers.URLField(max_length=700)
    is_new_notice = serializers.BooleanField(default=False)
class SyllabusSerializer(serializers.Serializer):
    head = serializers.CharField(max_length=200)
    url = serializers.URLField(max_length=700)
    is_new_notice = serializers.BooleanField(default=False)
class ExtraNoticeSerializer(serializers.ModelSerializer):
        class Meta:
          model = ExtraNotice
          fields = ["title", "url", "date","is_image"]
