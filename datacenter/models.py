from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
    
    def get_duration(self):
        delta = localtime() - self.entered_at
        seconds = delta.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        duration = '{} hours {} minutes'.format(int(hours), int(minutes))
        return duration
    
    def is_strange(self):
        limit_for_minutes = 60
        delta = self.leaved_at - self.entered_at
        seconds = delta.total_seconds()
        minutes = (seconds % 3600) // 60
        hours = seconds // 3600

        is_strange = minutes > limit_for_minutes or hours >= 1
        return is_strange