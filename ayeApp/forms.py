from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='', max_length=128,
                           widget= forms.TextInput
                           (attrs={'class':'form-control','placeholder': 'Email',
				   'id':'email'}))

class GuestsForm(forms.Form):
    guest_checkbox = forms.BooleanField(label='Name',widget=forms.CheckboxInput(attrs={'class':'container-guest-elements'}))
