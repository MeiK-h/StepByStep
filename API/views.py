#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Org.models import Org
from Step.models import Step

#查询所有Org
def GetOrgList(request):
    orgs = Org.objects.all()
    orgList = []
    for i in orgs:
        s = {}
        s['id'] = i.id
        s['name'] = i.name
        s['shortName'] = i.shortName
        orgList.append(s)
    returnData = {
        "status": True,
        "count": len(orgs),
        "list": orgList
    }
    return JsonResponse(returnData)

#获取指定Org的Step列表
def GetStepList(request):
    orgId = request.GET.get('orgId', '0')
    org = Org.objects.filter(id = int(orgId))
    if len(org) == 0:
        return JsonResponse({"status": False, "msg": "Org不存在"})
    step = Step.objects.filter(orgId = int(orgId))
    stepList = []
    for i in step:
        s = {}
        s['id'] = i.id
        s['title'] = i.title
        s['userCount'] = i.userCount
        s['problemCount'] = i.problemCount
        s['allAcCount'] = i.allAcCount
        stepList.append(s)
    returnData = {
        "status": True,
        "count": len(org),
        "orgId": org[0].id,
        "orgName": org[0].name,
        "shortName": org[0].shortName,
        "list": stepList
    }
    return JsonResponse(returnData)