from django.contrib import admin
from ayeApp.models import Invitation
from django.contrib.auth.models import Group,User

# Register your models here.

class InvitationForm(admin.ModelAdmin):

    fields = ['invitation_owner_name', 'email', 'telephone', 'guest_names', 'number_of_guests']
    #exclude = ('guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP',)
    #search_fields = ['invitation_owner_name']

    list_filter = ['is_RSVP']

    list_display = ['invitation_owner_name',  'email', 'telephone',  'guest_names', 'number_of_guests', 'guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP']


admin.site.register(Invitation, InvitationForm)
admin.site.unregister(Group)
