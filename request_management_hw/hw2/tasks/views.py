from .models import *
from django.http import HttpResponse

def list_create_tasks(request):
    if request.method == 'GET':
        query = Task.objects.order_by('name')
        return HttpResponse('<br>'.join(map(str, query)))


def count_tasks(request):
    if request.method == 'GET':
        number = Task.objects.count()
        msg = 'You have \'{}\' tasks to do'.format(number)
        return HttpResponse(msg)

