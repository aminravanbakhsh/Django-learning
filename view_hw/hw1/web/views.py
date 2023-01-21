from django.http import HttpResponse

def sad_msg_sender(request, name):
    msg = f"Nobody likes you, {name}!"
    return HttpResponse(msg)

def happy_msg_sender(request, name, num):
    msg = ""
    for i in range(num):
        msg += f"You are great, {name} :)<br>"
    
    return HttpResponse(msg)