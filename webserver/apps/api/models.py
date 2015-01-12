# -*- coding:utf-8 -*-
from django.db import models


class LocalBoxProxyAddress(models.Model):
  box_id = models.CharField(max_length=512, primary_key=True)
  address = models.CharField(max_length=512, null=True)
  class Meta:
    db_table = 'ygg_localbox_proxy_address'