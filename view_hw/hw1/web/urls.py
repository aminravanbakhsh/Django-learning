from django.urls import path

from .views import happy_msg_sender, sad_msg_sender

urlpatterns = [
    path('sad/<str:name>/', sad_msg_sender),
    path('happy/<str:name>/<int:num>/', happy_msg_sender)
]
