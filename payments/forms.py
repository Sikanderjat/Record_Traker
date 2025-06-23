from django import forms
from .models import Payment
from django.utils import timezone

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['item_name', 'quantity', 'payment_mode', 'bill', 'date_time'] 
        widgets = {
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'bill': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'item_name': 'Item Name',  # Ensure label matches
            'quantity': 'Quantity',
            'payment_mode': 'Payment Mode',
            'bill': 'Amount',
            'date_time': 'Date and Time',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Only set default for new instances
            now_local = timezone.localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')
            self.initial['date_time'] = now_local

class DateRangeForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Start Date'
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='End Date'
    )