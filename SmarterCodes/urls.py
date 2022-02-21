from django.contrib import admin
from django.urls import path, include

# Registered application assesment's urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assesment.urls')),
]

# default error pages are pointed towards custom_error view for error logging to admin email
handler500 = "assesment.views.custom_error"
handler400 = "assesment.views.custom_error"
handler403 = "assesment.views.custom_error"
handler404 = "assesment.views.custom_error"