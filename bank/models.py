from django.db import models


# Create your models here.
class BankLogs(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class BankLogsUTC(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

