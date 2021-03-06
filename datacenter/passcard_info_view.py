from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)

    all_visits = []
    for visit in visits_by_passcard:
        entered_at = visit.entered_at
        if visit.leaved_at:
            duration = visit.leaved_at - visit.entered_at
        elif not visit.leaved_at:
            duration = visit.get_duration()
        is_long_visit = visit.is_strange()
        titles = dict.fromkeys(['entered_at', 'duration', 'is_strange'])
        visits_info = [entered_at, duration, is_long_visit]
        info_view = dict(zip(titles, visits_info))
        all_visits.append(info_view)

    this_passcard_visits = all_visits

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
