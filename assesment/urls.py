from django.urls import path
from . import views

urlpatterns = [
    path('start_date=<str:start_date>/end_date=<str:end_date>', views.details, name='filtered_details'),
    path('', views.details, name='details'),
    path('load', views.load_data, name='load_data'),
]
