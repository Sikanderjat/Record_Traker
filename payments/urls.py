from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path('today/', views.today_payments, name='today_payments'),
    path('payments/', views.all_payments, name='all_payments'), 
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/range/', views.payments_in_range, name='payments_in_range'),
    path('payments/edit/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('payments/delete/<int:payment_id>/', views.delete_payment, name='delete_payment'),
]
