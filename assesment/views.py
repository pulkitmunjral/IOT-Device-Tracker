from django.shortcuts import render, redirect
from .models import Data
import requests
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def details(request, start_date=None, end_date=None):
    if request.method == "POST" and 'action' in request.POST:
        if request.POST['action'] == "submit":
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
        elif request.POST['action'] == "reset":
            return redirect("details")
    if start_date is None or end_date is None or start_date == "" or end_date == "":
        start_date, end_date, context = False, False, False
    elif cache.get(start_date+end_date):
        context = cache.get(start_date+end_date)
        print("from cache")
    else:
        context = Data.objects.filter(time_stamp__lte=end_date, time_stamp__gte=start_date).order_by('time_stamp')
        cache.set(start_date+end_date, context)
        print("from db")
    return render(request, "details.html", {'context': context, 'start_date': start_date, 'end_date': end_date})


def load_data(request):
    mock_endpoint = "https://61c6effa9031850017547293.mockapi.io/api/v2/iotmock"
    try:
        response = requests.get(mock_endpoint)
        json_response = response.json()
        for item in json_response:
            site_name = item['site_name']
            latitude = item['latitude']
            longitude = item['longitude']
            datastream = item['datastream']
            ip_address = item['ip_address']
            timestamp = item['timestamp']

            date_time_obj = datetime.strptime(timestamp, '%m/%d/%Y')
            timestamp = date_time_obj.strftime('%Y-%m-%d')
            data_object = Data(site_name=site_name, latitude=latitude, longitude=longitude,
                                      ip_address=ip_address, time_stamp=timestamp, dataframe=str(len(datastream)))
            data_object.save()
    except Exception as e:
        custom_error(e)
        print(e)
    return redirect('details')


def custom_error(request, *args, **argv):
    if request.method == "POST" and 'action' in request.POST and request.POST['action'] == "redirect":
        return redirect('details')
    try:
        subject = 'The website ran into trouble!!'
        message = f'Hi , SmaterCode assesmet sever ran into trouble by error {args} and {argv}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['pulkit.munjral@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        print("ran into error while sending email ",e)
        return render(request, 'custom_error.html')

    return render(request, 'custom_error.html')



# from rest_framework.generics import GenericAPIView
# from .serializers import DataSerializer
# class details(GenericAPIView):
#     serializer_class = DataSerializer
#
#     def post(self, request, start_date=None, end_date=None):
#         if request.method == "POST" and 'action' in request.POST:
#             if request.POST['action'] == "submit":
#                 start_date = request.POST['start_date']
#                 end_date = request.POST['end_date']
#             elif request.POST['action'] == "reset":
#                 return redirect("details")
#         if start_date is None or end_date is None or start_date == "" or end_date == "":
#             start_date, end_date, context = False, False, False
#         elif cache.get(start_date+end_date):
#             context = cache.get(start_date+end_date)
#             print("from cache")
#         else:
#             context = Data.objects.filter(timestamp__lte=end_date, timestamp__gte=start_date).order_by('timestamp')
#             cache.set(start_date+end_date, context)
#             print("from db")
#         return render(request, "details.html", {'context': context, 'start_date': start_date, 'end_date': end_date})
