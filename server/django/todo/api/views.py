from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Todo, Designer, Comment
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
import json

def todo(request):
     todos = Todo.objects.all()
     data = []
     each_todo = []
     for todo in todos:
        data.append({
            "requested_by": todo.requested_by.username,
            "project_number": todo.project_number,
            "position_number": todo.position_number,
            "status": todo.status,
            "department": todo.requested_by.groups.all()[0].name,
            "project_detail": todo.project_detail,
            "meeting": todo.meeting
        })
     print(data)
     return JsonResponse(data, encoder=JSONEncoder, safe=False)

@csrf_exempt
def add_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        return JsonResponse({"status": "ok"}, encoder=JSONEncoder)
    if request.method == "GET":
        print("wrong request")
