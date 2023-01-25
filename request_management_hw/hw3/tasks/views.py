from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        task = Task(name=task_name)
        task.save()

        msg = "Task Created: '{}'".format(task)
        return HttpResponse(msg)
