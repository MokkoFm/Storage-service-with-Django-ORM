from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)

    all_visits = []
    for visit in visits_by_passcard:
        if visit.leaved_at:
            passcard = visit.passcard
            entered_at = visit.entered_at
            duration = visit.leaved_at - visit.entered_at
            is_long_visit = visit.is_visit_long
            keys = dict.fromkeys(['entered_at', 'duration', 'is_strange'])
            vals = [entered_at, duration, is_long_visit]
            zipped = dict(zip(keys, vals))
            all_visits.append(zipped)

    this_passcard_visits = all_visits

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
