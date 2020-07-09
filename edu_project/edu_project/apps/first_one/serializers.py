from rest_framework import serializers

from first_one.models import Banner, Nav


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("img", 'link')
class NavModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ("is_site", 'link')

