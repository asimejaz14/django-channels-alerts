from datetime import timedelta

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .models import BankLogs, BankLogsUTC
from django.http import HttpResponse

import zoneinfo
from django.utils import timezone

from .serializers import BankLogSerializer

channel_name_mapping = {}


# Create your views here.
class BankAPIView1(APIView):

    @classmethod
    def get(cls, request):


        asia_karachi = zoneinfo.ZoneInfo("Asia/Karachi")
        with timezone.override(asia_karachi):

            converted_timezone_queryset = BankLogs.objects.filter(
                created_at__date=timezone.now().date() - timedelta(days=1)
            )
            pagination = LimitOffsetPagination()
            converted_timezone_queryset = pagination.paginate_queryset(converted_timezone_queryset, request)
            res = BankLogSerializer(converted_timezone_queryset, many=True).data

        asia_karachi = zoneinfo.ZoneInfo("Australia/Sydney")
        with timezone.override(asia_karachi):

            converted_timezone_queryset = BankLogs.objects.filter(
                created_at__date=timezone.now().date() - timedelta(days=1)
            )
            pagination = LimitOffsetPagination()
            converted_timezone_queryset = pagination.paginate_queryset(converted_timezone_queryset, request)
            res = BankLogSerializer(converted_timezone_queryset, many=True).data

        asia_karachi = zoneinfo.ZoneInfo("Canada/Central")
        with timezone.override(asia_karachi):

            converted_timezone_queryset = BankLogs.objects.filter(
                created_at__date=timezone.now().date() - timedelta(days=1)
            )
            pagination = LimitOffsetPagination()
            converted_timezone_queryset = pagination.paginate_queryset(converted_timezone_queryset, request)
            res = BankLogSerializer(converted_timezone_queryset, many=True).data

        converted_timezone_queryset = BankLogs.objects.filter(
            created_at__date=timezone.now().date() - timedelta(days=1)
        )
        pagination = LimitOffsetPagination()
        converted_timezone_queryset = pagination.paginate_queryset(converted_timezone_queryset, request)
        res = BankLogSerializer(converted_timezone_queryset, many=True).data

        return {}
        # return Response(None, status=HTTP_200_OK)
        # return HttpResponse("There is some data", status=HTTP_200_OK)


class BankAPIView2(APIView):

    @classmethod
    def post(cls, request):
        print(request.data)
        data = request.data.get('data')
        user = "Asim"
        user_id = "Asim"

        # Send data to the specific user's WebSocket
        channel_layer = get_channel_layer()
        channel_name = channel_name_mapping.get(user_id)
        if channel_name:
            async_to_sync(channel_layer.send)(channel_name, {
                "type": "send_alert",
                "message": data
            })

        return Response("Data Received.", status=status.HTTP_200_OK)

