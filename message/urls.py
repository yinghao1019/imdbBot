from django.urls import path
from message import views


urlpatterns = [
    path("reply",views.LineReply)

]