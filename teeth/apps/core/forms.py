from django import forms
from django.contrib.auth.models import User

from .uniqueNumber import callNum
from .new_user import UserCreationForm
from .models import Profile, Appointment, Details, Address, Occupation, Medical
from .choices import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial=callNum)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ()
        #fields = ('')

    def clean(self):
        tmpdata = self.cleaned_data.get('allowed_amount')
        profiles = self.cleaned_data.get('profiles')
        if profiles and profiles.count() > tmpdata:
            raise ValidationError('Maximum allowed profiles.')

        return self.cleaned_data

class DetailsForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Хүйс',choices = GENDER_CHOICES, required=True)
    class Meta:
        labels = {
        "family_name": "Овог",
        "first_name": "Эцэг эхийн нэр",
        "last_name": "Нэр",
        "register_num": "Регистрийн дугаар",
        "gender": "Хүйс",
        "phone_number": "Утасны дугаар",
        "emd_number": "ЭМД дугаар",
        "emd_type": "ЭМД төрөл",
        "ndd_number": "НДД дугаар",
        "erkhiin_bichig": "Эрхийн бичиг"
        }
        model = Details
        fields = ('family_name', 'first_name', 'last_name', 'register_num',
            'gender','phone_number','emd_number','emd_type','ndd_number','erkhiin_bichig')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('aimag_hot', 'sum_duureg', 'bag_horoo', 'horoolol_gudamj', 'bair_hashaa', 'toot')

class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ('bolovsrol', 'ajil', 'alban_tushaal', 'mergejil', 'baiguullaga', 'erheldeg_ajil', 'hariyalal')

class MedicalForm(forms.ModelForm):
    class Meta:
        model = Medical
        fields = ('tsusni_buleg', 'em_buleg', 'heregledeg_jsa', 'tolov','arhag_ovchin1', 'arhag_ovchin2', 'arhag_ovchin3','arhi_uudag', 'tamhi_tatdag', 'orhiin_emch', 'gerleltiin_baidal')

class AppointmentNewForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'allowed_amount', 'is_done')