from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from teeth.apps.core import views as core_views

urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^signup/$', core_views.signup, name='signup'),
	url(r'^signup1/$', core_views.add_details, name='add_details'),
	url(r'^signup2/$', core_views.add_address, name='add_address'),
	url(r'^signup3/$', core_views.add_occupation, name='add_occupation'),
	url(r'^signup4/$', core_views.add_medical, name='add_medical'),
	url(r'^$', core_views.home, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'profile/', core_views.user_profile, name='user_profile'),
	url(r'staff/', core_views.admin_profile, name='admin_profile'),
	
	url(r'^newAppointment/$', core_views.add_appointment, name='add_appointment'),

	url(r'^list/(?P<pk>\d+)/$', core_views.appointment_list, name='appointment_list'),
	url(r'^status/(?P<pk>\d+)/$', core_views.appointment_status, name='appointment_status'),
	url(r'^new/(?P<pk>\d+)/$', core_views.register_appointment, name='register_appointment'),
	url(r'^activate/$', core_views.confirm_first_activation, name='confirm_first_activation'),

	url(r'^user/', include('teeth.apps.core.urls')),
]
