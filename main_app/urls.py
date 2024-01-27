from django.urls import path
from main_app.views import home, service, members

urlpatterns = [
    path('',home,name='home_page'),
    path('service/',service,name='service_page'),
    path('members/',members,name='membe_page')
]
