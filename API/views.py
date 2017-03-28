#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Org.models import Org
from Step.models import Step
from API.models import *

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

#获取某人参加的所有计划
def GetUserStepList(request):
    source = request.GET.get('source', '')
    userName = request.GET.get('source', '')
    if source and userName:
        stepList = getUserStepList_M(source, userName)
        return JsonResponse({"status": True, "stepList": stepList})
    return JsonResponse({"status": False, "msg": "信息不足"})

#获取某计划的参与用户
def GetStepUser(request):
    stepId = request.GET.get('stepId', '')
    if stepId:
        userList = getStepUser(int(stepId))
        return JsonResponse({"status": True, "userList": userList})
    return JsonResponse({"status": False, "msg": "信息不足"})