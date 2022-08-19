from django.urls import path
from .views import reservation_list,update_reservation,contact_func,update_contact

app_name = 'manager'

urlpatterns=[
    path('reservations/',reservation_list,name="reservations_list"),
    path("reservations/update/<int:pk>/",update_reservation,name="update_reservation"),
    path("contacts/",contact_func,name="contact_func"),
    path("contacts/update/<int:pk>/",update_contact,name="update_contact"),
]