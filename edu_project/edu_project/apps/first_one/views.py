from rest_framework.generics import ListAPIView

from first_one.models import Banner, Nav
from first_one.serializers import BannerModelSerializer, NavModelSerializers


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer


class BannerListAPIViews(ListAPIView):
        queryset = Nav.objects.filter(is_show=True, is_delete=False).order_by("-orders")
        serializer_class = NavModelSerializers
