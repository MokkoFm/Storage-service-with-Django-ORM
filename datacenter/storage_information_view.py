from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import datetime


def storage_information_view(request):
    visits = Visit.objects.all()
    active_visits = []

    for visit in visits:
        if visit.entered_at and not visit.leaved_at:
            passcard = visit.passcard
            who_entered = passcard.owner_name
            entered_at = visit.entered_at
            duration = visit.get_duration()
            titles = dict.fromkeys(['who_entered', 'entered_at', 'duration'])
            visit_info = [who_entered, entered_at, duration]
            info_view = dict(zip(titles, visit_info))
            active_visits.append(info_view)

    non_closed_visits = active_visits
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
