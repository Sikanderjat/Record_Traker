# Generated by Django 5.2.3 on 2025-06-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_payment_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_mode',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('paid to Nanu', 'Paid to person1'), ('paid to Lala', 'Paid to Lala')], default='unpaid', max_length=20),
        ),
    ]
