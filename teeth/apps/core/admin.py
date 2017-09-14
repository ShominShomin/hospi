from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Appointment, Details, Address, Occupation, Medical
from .forms import AppointmentForm, DetailsForm, AddressForm, OccupationForm, MedicalForm

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username','first_name', 'last_name', 'is_staff','get_activeFirst','get_activeSecond')
    list_select_related = ('profile', )

    def get_activeFirst(self, instance):
        return instance.profile.is_activeFirst
    get_activeFirst.short_description = 'activeFirst'

    def get_activeSecond(self, instance):
        return instance.profile.is_activeSecond
    get_activeFirst.short_description = 'activeSecond'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm

class DetailsAdmin(admin.ModelAdmin):
    form = DetailsForm

class AddressAdmin(admin.ModelAdmin):
    form = AddressForm

class OccupationAdmin(admin.ModelAdmin):
    form = OccupationForm

class MedicalAdmin(admin.ModelAdmin):
    form = MedicalForm

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Occupation, OccupationAdmin)
admin.site.register(Medical, MedicalAdmin)