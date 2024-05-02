from rest_framework import serializers

from bank.models import BankLogs, BankLogsUTC


class BankLogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = BankLogs


class BankLogUTCSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = BankLogsUTC