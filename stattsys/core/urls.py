from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls") ), # login, logout, password views
    path('stattsys/', include('stattsys.urls')), #to ensure urls start with /stattsys/etc..
    

]
