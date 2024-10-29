from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index,name='home'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('', views.login,name='login'),
    path('admin_logout/', views.logout_admin,name='logout'),
    # path('indo/',views.indo,name='indo'),
    path('doctor_views/',views.doctor_view,name='doctor'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('delete_doctor/<int:id>',views.delete_doctor,name='delete_doctor'),
    path('patient_views/',views.patient_view,name='patient'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('delete_patient/<int:id>',views.delete_patient,name='delete_patient'),
    path('appointment_views/',views.appointment_view,name='appointment'),
    path('add_appointment/',views.add_appointment,name='add_appointment'),
    path('delete_appointment/<int:id>',views.delete_appointment,name='delete_appointment'),
]