from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from . import forms
from ayeApp.models import  Invitation
from datetime import datetime, timedelta


# Create your views here.

def index(request):
    email_form = forms.EmailForm()
    # guests_form = forms.GuestsForm()
    return render(request, 'rsvpApp/index.html', {'email_form': email_form})

def ajax_call(request):
    if request.method == 'GET':
        email = request.GET.get('email', None)
        data = {
             'is_there': Invitation.objects.filter(email__exact=email).exists()
         }
        if data['is_there']:
            emailID = Invitation.objects.get(email__exact=email)
            data['guests'] = Invitation.objects.get(email=email).guest_names
            data['confirmed'] = Invitation.objects.get(email=email).guests_confirmed
            data['name'] = Invitation.objects.get(email = email).invitation_owner_name
            data['no_of_guests'] = Invitation.objects.get(email=email).number_of_guests

        else:
            data['error_message'] = 'No existe el correo ingresado en la base de datos.'


        return JsonResponse(data)

    else:
        names_to_saved = request.POST.get('guests', None)
        invitation_size = names_to_saved.split(",")
        email = request.POST.get('email', None)
        invitationRecord = Invitation.objects.get(email__exact=email)

        if (names_to_saved):
            invitationRecord.guests_confirmed = names_to_saved
            invitationRecord.total_guests_confirmed = len(invitation_size)
        else:
            invitationRecord.guests_confirmed = None
            invitationRecord.total_guests_confirmed = 0

        invitationRecord.is_RSVP = True
        invitationRecord.date_RSVP = (datetime.now()) - (timedelta(hours=4, minutes=00))
        invitationRecord.save()


        return HttpResponse("Success!")
