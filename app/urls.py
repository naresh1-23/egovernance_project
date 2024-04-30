from django.urls import path
from . import views


urlpatterns = [
    path('child_register/', views.birth_certificate, name='child-register'),
    path('father/', views.fathers_detail, name='father-register'),
    path('mother/', views.mothers_detail, name='mother-register'),
    path('confirmation_person/', views.confirmation_detail, name='confirmation-person-register'),
    path('get_detail/<int:id>/', views.get_details, name='get-detail')
]
