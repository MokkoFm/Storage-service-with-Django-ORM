from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import datetime


def storage_information_view(request):
    passcards = Passcard.objects.all()
    visits = Visit.objects.all()

    for passcard in passcards:
        for visit in visits:
            passcard = visit.passcard
            entered_at = visit.entered_at
            duration = visit.get_duration

            if visit.entered_at and not visit.leaved_at:
                who_entered = passcard.owner_name
            

    non_closed_visits = [
        {
            "who_entered": who_entered,
            "entered_at": entered_at,
            "duration": duration, 
        }
    ]
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
