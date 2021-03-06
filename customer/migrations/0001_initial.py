# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('address', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=40)),
                ('province', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('country', models.CharField(max_length=40)),
                ('postal_code', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('email', models.CharField(max_length=60)),
                ('support_rep', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.Employee')),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField()),
                ('billing_address', models.CharField(max_length=70)),
                ('billing_City', models.CharField(max_length=40)),
                ('billing_tate', models.CharField(max_length=40)),
                ('billing_Country', models.CharField(max_length=40)),
                ('billing_postal_code', models.CharField(max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Invoice')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.Track')),
            ],
        ),
    ]
