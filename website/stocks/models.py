from django.db import models
from datetime import datetime


class ClientOneToOne(models.Model):
    field_20 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_22a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_22c = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_30t = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_52a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_82a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_87a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_77h = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_30v = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_36 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_32b = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_57a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_33b = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_53a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_56 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_57d = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_58a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_24d = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.



class SgOneToOne(models.Model):
    field_20 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_22a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_22c = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_30t = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_52a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_82a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_87a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_77h = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_30v = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_36 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_32b = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_57a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_33b = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_53a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_56 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_57d = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_58a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_24d = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    

class matched(models.Model):
    client = models.ForeignKey(ClientOneToOne, on_delete=models.CASCADE)
    sg = models.ForeignKey(SgOneToOne, on_delete=models.CASCADE)
    status=models.TextField(null=False)