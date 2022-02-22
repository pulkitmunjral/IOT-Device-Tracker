from django.shortcuts import render, redirect
from .models import Data
import requests
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from rest_framework.generics import GenericAPIView
from .serializers import DataSerializer

# getting timeout vale from app setting
# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class Details(GenericAPIView):
    # Main page route defined as rest api class
    serializer_class = DataSerializer

    # route for get response
    def get(self, request, start_date=None, end_date=None):

        #   Handling any invalid value for start_date and end_date
        if start_date is None or end_date is None or start_date == "" or end_date == "":
            start_date, end_date, context = False, False, False

        #   checking if data is already present in cache server
        elif cache.get(start_date+end_date):
            context = cache.get(start_date+end_date)
            print("from cache")

        #   Fetching data from db from start_date to end_date inclusive, ordered by time, stored in context variable
        else:
            # storing data to cache server
            context = Data.objects.filter(time_stamp__lte=end_date, time_stamp__gte=start_date).order_by('time_stamp')
            cache.set(start_date+end_date, context)

        #   returning the details template with data variables
        return render(request, "details.html", {'context': context, 'start_date': start_date, 'end_date': end_date})

    #   route for post response
    def post(self, request, start_date=None, end_date=None):

        #   validating action requested
        if 'action' in request.POST:
            if request.POST['action'] == "submit":

                #   getting start_date and end_date variables from request
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']

            #   reset route back to main page
            elif request.POST['action'] == "reset":
                return redirect("details")

            #   kept else block for future use
            else:
                pass

        #   kept else block for future use
        else:
            pass

        #   returning get route with variables for html response
        return self.get(request, start_date, end_date)


class LoadData(GenericAPIView):
    #   rest api class for loading data every hour triggered from cron job
    #   cron job expression for every hour 59 */1 * * *
    def get(self, request):

        #   Defining mock endpoint url
        mock_endpoint = "https://61c6effa9031850017547293.mockapi.io/api/v2/iotmock"

        #   fetching data in try cache to log error msg directly to admin
        try:
            response = requests.get(mock_endpoint)
            json_response = response.json()

            #   looping over complete data set
            for item in json_response:
                site_name = item['site_name']
                latitude = item['latitude']
                longitude = item['longitude']
                datastream = item['datastream']
                ip_address = item['ip_address']
                timestamp = item['timestamp']

                #   converting timestamp to required format
                date_time_obj = datetime.strptime(timestamp, '%m/%d/%Y')
                timestamp = date_time_obj.strftime('%Y-%m-%d')

                #   creating Data object and storing it to db
                data_object = Data(site_name=site_name, latitude=latitude, longitude=longitude,
                                          ip_address=ip_address, time_stamp=timestamp, dataframe=str(len(datastream)))
                data_object.save()

        #   handling exception by raising issue to admin
        except Exception as e:
            custom_error(e)
            print(e)

        #   redirecting back to main page
        return redirect('details')


def custom_error(request, *args, **argv):
    #   custom error handling route
    #   loads the details page on getting redirect input from user
    if request.method == "POST" and 'action' in request.POST and request.POST['action'] == "redirect":
        return redirect('details')

    #   sending current issue log to admin
    try:
        subject = 'The website ran into trouble!!'
        message = f'Hi , SmaterCode assesmet sever ran into trouble by error {args} and {argv}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['pulkit.munjral@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        print("ran into error while sending email ", e)
        return render(request, 'custom_error.html')

    return render(request, 'custom_error.html')
