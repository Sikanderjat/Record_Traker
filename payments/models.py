from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Payment(models.Model):
    ITEM_NAMES = [
        ('Aarav Sharma', 'Aarav Sharma'),
        ('Priya Patel', 'Priya Patel'),
        ('Rohan Singh', 'Rohan Singh'),
        ('Neha Gupta', 'Neha Gupta'),
        ('Vikram Desai', 'Vikram Desai'),
        ('Anjali Mehta', 'Anjali Mehta'),
        ('Karan Joshi', 'Karan Joshi'),
        ('Sneha Reddy', 'Sneha Reddy'),
        ('Arjun Kapoor', 'Arjun Kapoor'),
        ('Divya Nair', 'Divya Nair'),
        ('Sameer Khan', 'Sameer Khan'),
        ('Ritu Malhotra', 'Ritu Malhotra'),
        ('Amit Verma', 'Amit Verma'),
        ('Pooja Iyer', 'Pooja Iyer'),
        ('Rajesh Kumar', 'Rajesh Kumar'),
        ('Kavita Shah', 'Kavita Shah'),
        ('Vikrant Chauhan', 'Vikrant Chauhan'),
        ('Shruti Mishra', 'Shruti Mishra'),
        ('Deepak Yadav', 'Deepak Yadav'),
        ('Sonia Thakur', 'Sonia Thakur'),
        ('Harsh Vohra', 'Harsh Vohra'),
        ('Meera Saxena', 'Meera Saxena'),
        ('Nikhil Bansal', 'Nikhil Bansal'),
        ('Tanvi Agarwal', 'Tanvi Agarwal'),
        ('Rahul Pandey', 'Rahul Pandey'),
        ('Aisha Qureshi', 'Aisha Qureshi'),
        ('Siddharth Bose', 'Siddharth Bose'),
        ('Lakshmi Rao', 'Lakshmi Rao'),
        ('Aditya Jain', 'Aditya Jain'),
        ('Zoya Hussain', 'Zoya Hussain'),
    ]

    PAYMENT_MODES = [
        ('unpaid', 'Unpaid'),
        ('paid to Nanu', 'Paid to Nanu'),
        ('paid to Lala', 'Paid to Lala'),
    ]

    item_name = models.CharField(max_length=50, choices=ITEM_NAMES, default='Aarav Sharma')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES , default='unpaid')
    date_time = models.DateTimeField(default=timezone.now)
    bill = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.item_name} - {self.payment_mode} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"