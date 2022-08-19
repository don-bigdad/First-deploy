from django.shortcuts import render,redirect
from base.models import ReservationForm,Contact
from django.contrib.auth.decorators import login_required,user_passes_test

def is_manager(user):
    return user.groups.filter(name="manager").exists()

@login_required(login_url="account/login/")
@user_passes_test(is_manager)
def reservation_list(request):
    not_reserv = ReservationForm.objects.filter(is_processed=False)
    return render(request, "reservation_list.html", context={
        "unreserv_list":not_reserv,
    }
        )
@login_required(login_url="account/login/")
@user_passes_test(is_manager)
def update_reservation(request,pk):
    ReservationForm.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:reservations_list")

@user_passes_test(is_manager)
def contact_func(request):
    unreviewed=Contact.objects.filter(done=False)
    return render(request,"contacts.html",context={
        "unreview_message":unreviewed,
    }
      )
@user_passes_test(is_manager)
def update_contact(request,pk):
    Contact.objects.filter(pk=pk).update(done=True)
    return redirect("manager:contact_func")