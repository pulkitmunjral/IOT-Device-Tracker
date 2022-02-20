from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import RedirectView

schema_view = get_swagger_view(title="anything")

urlpatterns = [
    path('', RedirectView.as_view(url='details/')),
    path('details/start_date=<str:start_date>/end_date=<str:end_date>', views.Details.as_view(), name='filtered_details'),
    path('details/', views.Details.as_view(), name='details'),
    path('load', views.LoadData.as_view(), name='load_data'),
    path('swagger', schema_view),
]
