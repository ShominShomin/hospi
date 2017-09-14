from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone

from .models import Profile, Appointment, Details, Address, Occupation, Medical
from .forms import AppointmentForm, DetailsForm, AddressForm, OccupationForm, MedicalForm, SignUpForm, AppointmentNewForm
 
def home(request):
    return render(request, 'core/home.html')

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    appointments = Appointment.objects.filter(published_date__lte=timezone.now(), is_done=False).order_by('-published_date')
    appointment_searched = Appointment.objects.filter(is_done=False, profiles = Profile.objects.get(user=request.user))

    if appointment_searched.exists():
        schedule = appointment_searched[:1].get().title
    else:
        schedule = 'Хуваарь аваагүй.'

    paginator = Paginator(appointments, 5)
    page = request.GET.get('page', 1)  
    appointments = paginator.page(page)  

    time_activate= profile.created_date + timedelta(days=14)
    time_check = False
    if time_activate < timezone.now():
        time_check = True

    context = {
        'profile': profile,
        'appointments': appointments,
        'schedule': schedule,
        'time': time_activate,
        'time_check': time_check
    }
    template = 'registration/user_profile.html'  
    return render(request, template, context)

@login_required
def register_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment_searched = Appointment.objects.filter(is_done=False, profiles = Profile.objects.get(user=request.user))
     
    if not appointment_searched:
        if appointment.profiles.count() < appointment.allowed_amount:
            profile = Profile.objects.get(user=request.user)
            appointment.profiles.add(profile)
            return redirect(request.META['HTTP_REFERER'])
        else:
            error = "Таны хуваарь авах гэж буй өдөр дүүрэн байна."
    else:
        error = "Та аль хэдийн хуваарь авсан байна."

    return render(request, 'passage/empty.html', {'error': error})
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('user_profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            details = form.save()
            user = request.user
            user.profile.details = details
            user.save()
            details.save()
            
            if user.profile.address is None:
                return redirect('add_address')
            elif user.profile.occupation is None:
                return redirect('add_occupation')
            elif user.profile.medical is None:
                return redirect('add_medical')
            else:
                return redirect('user_profile')

    else:
        form = DetailsForm()
    return render(request, 'registration/signup2.html', {'form': form})    

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            user = request.user
            user.profile.address = address
            user.save()
            address.save()

            if user.profile.details is None:
                return redirect('add_details')
            elif user.profile.occupation is None:
                return redirect('add_occupation')
            elif user.profile.medical is None:
                return redirect('add_medical')
            else:
                return redirect('user_profile')
    else:
        form = AddressForm()
    return render(request, 'registration/signup2.html', {'form': form})    

@login_required
def add_occupation(request):
    if request.method == 'POST':
        form = OccupationForm(request.POST)
        if form.is_valid():
            occupation = form.save()
            user = request.user
            user.profile.occupation = occupation
            user.save()
            occupation.save()
            
            if user.profile.details is None:
                return redirect('add_details')
            elif user.profile.address is None:
                return redirect('add_address')
            elif user.profile.medical is None:
                return redirect('add_medical')
            else:
                return redirect('user_profile')
    else:
        form = OccupationForm()
    return render(request, 'registration/signup2.html', {'form': form})

@login_required
def add_medical(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            medical = form.save()
            user = request.user
            user.profile.medical = medical
            user.save()
            medical.save()
            
            if user.profile.details is None:
                return redirect('add_details')
            elif user.profile.address is None:
                return redirect('add_address')
            elif user.profile.occupation is None:
                return redirect('add_occupation')
            else:
                return redirect('user_profile')
    else:
        form = MedicalForm()
    return render(request, 'registration/signup2.html', {'form': form})     

@staff_member_required
def admin_profile(request):
    appointment_list = Appointment.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(appointment_list, 10)
    page = request.GET.get('page', 1)
    
    appointments = paginator.page(page)  
    return render(request, 'appointment/admin_profile.html', {'appointments': appointments})


@staff_member_required
def appointment_list(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    return render(request, 'appointment/list.html', {'appointments': appointment})

@staff_member_required
def appointment_status(request, pk):
    appointment = Appointment.objects.get(pk=pk)

    if appointment.is_done:
        appointment.is_done= not appointment.is_done
        appointment.save()
    else:
        appointment.is_done= not appointment.is_done
        appointment.save()

    return redirect(request.META['HTTP_REFERER'])


@staff_member_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentNewForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('admin_profile')
    else:
        form = AppointmentNewForm()
    return render(request, 'registration/signup2.html', {'form': form})     

@login_required
def confirm_first_activation(request):
    profile = Profile.objects.get(user=request.user)

    if profile.created_date + timedelta(days=14) < timezone.now():
        profile.is_activeFirst = True
        profile.save()

    return redirect(request.META['HTTP_REFERER'])
