# Generated by Django 2.0.9 on 2018-12-15 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('limit_balance', models.IntegerField(default=100000)),
                ('sex', models.IntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('education', models.IntegerField(choices=[(1, 'graduate_school'), (2, 'university'), (3, 'high_school'), (4, 'other')], default=1)),
                ('marriage', models.IntegerField(choices=[(1, 'married'), (2, 'single'), (3, 'others')], default=1)),
                ('age', models.IntegerField()),
                ('pay_0', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('pay_2', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('pay_3', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('pay_4', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('pay_5', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('pay_6', models.IntegerField(choices=[(-1, 'pay early'), (0, 'pay dully'), (1, '1month_dalay'), (2, '2months_dlay')], default=0)),
                ('bill_amt_1', models.IntegerField(default=0.0)),
                ('pay_amt_1', models.IntegerField(default=5000)),
                ('pay_amt_2', models.IntegerField(default=5000)),
                ('pay_amt_3', models.IntegerField(default=5000)),
                ('pay_amt_4', models.IntegerField(default=5000)),
                ('pay_amt_5', models.IntegerField(default=5000)),
                ('pay_amt_6', models.IntegerField(default=5000)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('proba', models.FloatField(default=0.0)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('registered_date', models.DateField(default=datetime.date(2018, 12, 15))),
            ],
        ),
    ]
