from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse


@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'GET':
        task = None
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            task = None

        if task != None:
            name = task.name
            task.delete()
            msg = "Task Done: \'{}\'".format(name)
            
        else:
            msg = "There isn't any task with id \'{}\'".format(task_id)

        return HttpResponse(msg)
