from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, SubTaskSerializer
from main.models import Card, SubCard, User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime


# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        "List Task":"http://127.0.0.1:8000/api/task-list/",
        "List SubTask": "http://127.0.0.1:8000/api/subtask-list/<str:doom>",
        "Create Task": "http://127.0.0.1:8000/api/task-create/",
        "Create SubTask": "http://127.0.0.1:8000/api/subtask-create/<str:doom>",
        "Delete Task": "http://127.0.0.1:8000/api/task-delete/",
        "Delete SubTask": "http://127.0.0.1:8000/api/subtask-delete/",
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks = Card.objects.filter(task_owner=request.user.id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def subTaskList(request, *args, **kwargs):
    id = request.query_params["id"]
    if id != None:
        subTask = SubCard.objects.filter(task_name=id)
        serializer = SubTaskSerializer(subTask, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    dash = request.data
    dd = datetime.datetime.strptime(dash["task_deadline_date"], '%Y-%m-%d')
    dt = datetime.datetime.strptime(dash["task_deadline_time"], '%H:%M:%S')
    ddt = datetime.datetime.combine(dd.date(), dt.time())
    jar = {'task_owner':request.user.id, "task_status":False, "task_urgency": "low", "task_progress": 0, "task_deadline":ddt}
    dash.update(jar)
    serializer = TaskSerializer(data=dash)


    if serializer.is_valid():
        serializer.save()
        

    return Response(":)")

@api_view(['POST', "GET"])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def subTaskCreate(request, doom):
    tn = doom
    dash = request.data
    jar = {"task_name":tn, "subtask_state":False}
    dash.update(jar)
    print(dash)
    serializer = SubTaskSerializer(data=dash)

    if serializer.is_valid():
        serializer.save()
        print("success")
    else:
        print("doomed")
        
        
    return Response(":)")



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def taskDelete(request, *args, **kwargs):
    id = request.query_params["id"]
    task = Card.objects.filter(taskid=id)
    task.delete()
    return Response(":(")


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def subTaskDelete(request, *args, **kwargs):
    id = request.query_params["id"]
    subTask = SubCard.objects.filter(id=id)
    subTask.delete()
    return Response(":(")