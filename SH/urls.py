from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('user/', views.User_list, name="Let's"),
    path('sensors/', views.ESPSensor_list),
    path('outputs/', views.ESPOut_list),
    
        
    path('espoutdetail/<int:esp_id>/', views.ESPOut_listdetail),
    path('espsensordetail/<int:esp_id>/', views.ESPSensor_listdetail),
    path('userespsensor/<int:user_id>/', views.ESPSensor_list),
    path('userespout/<int:user_id>/', views.ESPOut_list),
    path('userlogin/<path:login>/', views.GetUser),
    
    
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
