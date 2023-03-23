# Generated by Django 4.1.7 on 2023-03-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('fName', models.CharField(max_length=30)),
                ('mName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipCode', models.CharField(max_length=5)),
                ('homePhone', models.CharField(max_length=5)),
                ('cellPhone', models.CharField(max_length=5)),
                ('pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('startDate', models.DateTimeField(verbose_name='Start Date')),
                ('employeeID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
