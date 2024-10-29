from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login, logout
from .models import doctor,patient,Appointment
from django.db import IntegrityError
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse



# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def home(request):
    if not request:
        return redirect('login')
    return render(request, 'logout.html')

def login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
               login(request, user)
               error="No"
            else:
               error = "Yes"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'login.html', d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

# def indo(request):
#     if not request.user.is_staff:
#         return render(request,'login')
#     doctor = doctor.objects.all()
#     patient = patient.object.all()
#     appointment = appointment.object.all()
#     d=0
#     p=0
#     a=0
#     for i in doctor:
#         d+=1

#     for i in patient:
#         p+=1
        
#     for i in appointment:
#         a+=1
    
#     d1={'d':d,'p':p,'a':a}


           #DOCTOR

def doctor_view(request):
    if not request:
        return redirect('login')
    doc=doctor.objects.all()
    d={'doc':doc}
    return render(request,'doctor_view.html',d)



def delete_doctor(request, id):
    deldoc = doctor.objects.filter(id = id)[0]
    deldoc.delete()
    return HttpResponseRedirect('/doctor_views')

def add_doctor(request):
    error = ""
    if request.method.lower() == "post":
        na = request.POST.get('name')
        ca = request.POST.get('mobile')
        sp = request.POST.get('special')
        try:
            doctor.objects.create(name=na, mobile=ca, special=sp)
            error = "no"
        except Exception as e:
            error = f"yes: {str(e)}"
    else:
        error = "Invalid request method."

    d = {'error': error}
    return render(request, 'add_doctor.html', d)


           #PATIENTw



def patient_view(request):
    if not request:
        return redirect('login')
    doc=patient.objects.all()
    d={'doc':doc}
    return render(request,'patient_views.html',d)



def delete_patient(request, id):
    deldoc = patient.objects.filter(id = id)[0]
    deldoc.delete()
    return HttpResponseRedirect('/patient_views')




def add_patient(request):
    error = ""
    if not request:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST.get('name')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')

        try:
            patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = 'no'

        except IntegrityError:
            error = "Duplicate entry"

    d = {'error': error}
    return render(request, 'add_patient.html', d)




         #APPOINTMENT



def appointment_view(request):
    if not request:
        return redirect('login')
    doc=Appointment.objects.all()
    d={'doc': doc}
    return render(request,'appointment_views.html',d)




# def delete_appointment(request, pid):
#     if request.method == 'POST':
#         appointment_instance = get_object_or_404(Appointment, id=pid)
#         appointment_instance.delete()
#         return redirect('appointment_views')
#     else:
#         return redirect('login')
def delete_appointment(request, id):
    deldoc = Appointment.objects.filter(id = id)[0]
    deldoc.delete()
    return HttpResponseRedirect('/appointment_views')



def add_appointment(request):
    error = ""
    if not request:
        return redirect('login')
    
    Doctors = doctor.objects.all()
    Patients = patient.objects.all()
    if request.method == "POST":
        d_name = request.POST.get('doctor')
        p_name = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')
        disease = request.POST.get('disease')
        doctor_instance = doctor.objects.filter(name=d_name).first()
        patient_instance = patient.objects.filter(name=p_name).first()
        app = Appointment(Doctor=doctor_instance,Patient=patient_instance,date=date,time=time,disease=disease)
        app.save()    
    context = {'Doctors': Doctors, 'Patients': Patients, 'error': error}
    return render(request,'add_appointment.html',context)
