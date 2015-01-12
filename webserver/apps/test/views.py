# -*- coding:utf-8 -*-
from django.shortcuts import render
from webserver.apps.api.models import LocalBoxProxyAddress as LBPA

def test_localbox_proxy_address(request):
  items = LBPA.objects.all()
  return render(request, 'test_localbox_proxy_address.html', {'items': items})