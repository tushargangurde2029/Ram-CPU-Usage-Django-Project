"""from django.shortcuts import render
import psutil

# Create your views here.
def hello(request):     
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print('RAM memory % used:', psutil.virtual_memory()[2])
    return render(request,"homepage.html")"""

# from django.http import JsonResponse

import psutil   
from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
   
from rest_framework.views import APIView
from rest_framework.response import Response
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
   
   
####################################################
   
## if you don't want to user rest_framework
   
# def get_data(request, *args, **kwargs):
#
# data ={
#             "sales" : 100,
#             "person": 10000,
#     }
#
# return JsonResponse(data) # http response
   
   
#######################################################
   
## using rest_framework classes
   
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        labels = [
            'RAM',
            'CPU'
            ]
        chartLabel = "System Usage"
        cpu_usage = int(psutil.cpu_percent(4))
        ram_usage = int(psutil.virtual_memory()[2])
        chartdata = []
        chartdata.append(ram_usage)
        chartdata.append(cpu_usage)

        ram_data = [10,20,30,80,40,50]
        cpu_data = [5,34,23,2,70,100]

        chartlabel_ram = "RAM Usage"
        chartlabel_cpu = "CPU Usage"
        labels1 = ['2022-04-18 22:05:01','2022-04-18 22:05:02','2022-04-18 22:05:03','2022-04-18 22:05:04','2022-04-18 22:05:05','2022-04-18 22:05:06'] 
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
                     "labels1":labels1,
                     "ram_data":ram_data,
                     "cpu_data":cpu_data,
                     "chartlabel_ram":chartlabel_ram,
                     "chartlabel_cpu":chartlabel_cpu,
             }
        if ram_usage>50:
            subject = 'This is the alert for Ram Usage'
            message = ' Your RAM Usage is above 50%'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['tushargangurde405@gmail.com',]
            send_mail( subject, message, email_from, recipient_list ) 
        
        return Response(data)