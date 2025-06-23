from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm, DateRangeForm
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime, time, timedelta

def index(request):
    return render(request, 'index.html')

def today_payments(request):
    now = timezone.localtime(timezone.now())
    today = now.date()
    start_of_day = timezone.make_aware(datetime.combine(today, time(0, 0)), timezone.get_current_timezone())
    end_of_day = start_of_day + timedelta(days=1) - timedelta(microseconds=1)
    records = Payment.objects.filter(date_time__range=(start_of_day, end_of_day))
    totals = records.aggregate(total_sales=Sum('bill'), total_quantity=Sum('quantity'))
    total_sales = totals['total_sales'] or 0.00
    total_quantity = totals['total_quantity'] or 0
    
    # Calculate totals by payment mode
    mode_totals = records.values('payment_mode').annotate(
        mode_sales=Sum('bill'),
        mode_quantity=Sum('quantity')
    )
    unpaid_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'unpaid'), 0.00)
    person1_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person1'), 0.00)
    person2_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person2'), 0.00)
    
    return render(request, 'today_payments.html', {
        'records': records,
        'total_sales': total_sales,
        'total_quantity': total_quantity,
        'unpaid_sales': unpaid_sales,
        'person1_sales': person1_sales,
        'person2_sales': person2_sales,
        'current_page': 'today_payments'
    })

def all_payments(request):
    records = Payment.objects.all()
    totals = records.aggregate(total_sales=Sum('bill'), total_quantity=Sum('quantity'))
    total_sales = totals['total_sales'] or 0.00
    total_quantity = totals['total_quantity'] or 0
    
    # Calculate totals by payment mode
    mode_totals = records.values('payment_mode').annotate(
        mode_sales=Sum('bill'),
        mode_quantity=Sum('quantity')
    )
    unpaid_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'unpaid'), 0.00)
    person1_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person1'), 0.00)
    person2_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person2'), 0.00)
    
    return render(request, 'all_payments.html', {
        'records': records,
        'total_sales': total_sales,
        'total_quantity': total_quantity,
        'unpaid_sales': unpaid_sales,
        'person1_sales': person1_sales,
        'person2_sales': person2_sales,
        'current_page': 'all_payments'
    })

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('today_payments')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            redirect_page = request.POST.get('page', 'today_payments')
            return redirect(redirect_page)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {
        'form': form,
        'payment': payment,
        'page': request.GET.get('page', 'today_payments')
    })

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        redirect_page = request.POST.get('page', 'today_payments')
        payment.delete()
        return redirect(redirect_page)
    return redirect('today_payments')

def payments_in_range(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            start_datetime = timezone.make_aware(datetime.combine(start_date, time(0, 0)), timezone.get_current_timezone())
            end_datetime = timezone.make_aware(datetime.combine(end_date, time(23, 59, 59, 999999)), timezone.get_current_timezone())
            records = Payment.objects.filter(date_time__range=(start_datetime, end_datetime))
            totals = records.aggregate(total_sales=Sum('bill'), total_quantity=Sum('quantity'))
            total_sales = totals['total_sales'] or 0.00
            total_quantity = totals['total_quantity'] or 0
            
            # Calculate totals by payment mode
            mode_totals = records.values('payment_mode').annotate(
                mode_sales=Sum('bill'),
                mode_quantity=Sum('quantity')
            )
            unpaid_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'unpaid'), 0.00)
            person1_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person1'), 0.00)
            person2_sales = next((item['mode_sales'] or 0.00 for item in mode_totals if item['payment_mode'] == 'paid to person2'), 0.00)
            
            return render(request, 'range_payments.html', {
                'records': records,
                'form': form,
                'total_sales': total_sales,
                'total_quantity': total_quantity,
                'unpaid_sales': unpaid_sales,
                'person1_sales': person1_sales,
                'person2_sales': person2_sales,
                'current_page': 'payments_in_range'
            })
    else:
        form = DateRangeForm()
    return render(request, 'range_payments.html', {
        'form': form,
        'total_sales': 0.00,
        'total_quantity': 0,
        'unpaid_sales': 0.00,
        'person1_sales': 0.00,
        'person2_sales': 0.00,
        'current_page': 'payments_in_range'
    })