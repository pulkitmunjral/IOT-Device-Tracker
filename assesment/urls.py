from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SmarterCodes API",
      default_version='v1',
      description="testing for first time",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="uschat.cf@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('start_date=<str:start_date>/end_date=<str:end_date>', views.details, name='filtered_details'),
    path('', views.details, name='details'),
    path('load', views.load_data, name='load_data'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
