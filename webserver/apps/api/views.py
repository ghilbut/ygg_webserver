# -*- coding:utf-8 -*-
from django.utils import simplejson
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from webserver.apps.api.models import LocalBoxProxyAddress as LBPA


@csrf_exempt
def reg_localbox_proxy_address(request):
  if request.method != 'POST':
    raise Http404

  data = simplejson.loads(request.body)
  box_id = data['box-id']
  address = data['address']

  obj, created = LBPA.objects.get_or_create(box_id=box_id, defaults={'address': address})
  if not created:
    obj.address = address
    obj.save()

  ret = {'box-id': box_id, 'address': address}
  json = simplejson.dumps(ret)
  content_type = 'application/json'
  return HttpResponse(json, content_type=content_type, mimetype=content_type)


@csrf_exempt
def unreg_localbox_proxy_address(request):
  if request.method != 'POST':
    raise Http404

  data = simplejson.loads(request.body)
  box_id=data['box-id']
  ret = {'box-id': box_id}
 
  try:    
    obj = LBPA.objects.get(box_id=box_id)
    obj.delete()
  except LBPA.DoesNotExist:
    del ret['box-id']

  json = simplejson.dumps(ret)
  content_type = 'application/json'
  return HttpResponse(json, content_type=content_type, mimetype=content_type)