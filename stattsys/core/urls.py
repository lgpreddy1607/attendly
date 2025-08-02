from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stattsys/', include('stattsys.urls')), #to ensure urls start with /stattsys/etc..
    

]
