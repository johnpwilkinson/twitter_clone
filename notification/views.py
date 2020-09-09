from django.shortcuts import render
from .models import Notification



def notificationview(request):
    notifs = Notification.objects.filter(atted_person=request.user, read=False)
    for note in notifs:
        note.read = True
        note.save()
    return render(request, "notifications.html", {"notifs": notifs})

