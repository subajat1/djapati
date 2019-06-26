from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView

from webpush import send_user_notification

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class PayloadViewSet(APIView):
#     #permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

def subscribe(request):
    context = {}
    return render(request, 'djapati/subscribe.html', context)

def send_dummy(request):
    log = '{}: '.format(str(request.user))
    response = ''
    payload = {"head": "Welcome!", "body": "This is dummy notification. Plain and hard-coded!"}
    
    try:
        response = send_user_notification(user=request.user, payload=payload, ttl=1000)
        log = 'Notification sent. {}'.format(str(response))
    except:
        log = 'asdf failed send notification. {}'.format(str(response))

    # send_user_notification(user=request.user, payload=payload, ttl=1000)

    return HttpResponse(log)
    

# TODO: class PayloadViewSet(APIView)
# 
#  