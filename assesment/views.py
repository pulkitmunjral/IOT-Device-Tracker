from django.shortcuts import render, redirect
from .models import Data
import requests
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail


def details(request, start_date=None, end_date=None):
    if request.method == "POST" and 'action' in request.POST:
        if request.POST['action'] == "submit":
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
        elif request.POST['action'] == "reset":
            return redirect("details")
    if start_date is None or end_date is None or start_date == "" or end_date == "":
        start_date, end_date, context = False, False, False
    else:
        context = Data.objects.filter(timestamp__lte=end_date, timestamp__gte=start_date).order_by('timestamp')

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
                                      ip_address=ip_address, timestamp=timestamp)
            data_object.save()
    except Exception as e:
        msg(e)
        print(e)
    return redirect('details')


def msg(error):
    subject = 'The website ran into trouble!!'
    message = f'Hi , SmaterCode assesmet sever ran into trouble by error {error}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['pulkit.munjral@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)