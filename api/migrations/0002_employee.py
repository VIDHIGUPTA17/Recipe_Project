# Generated by Django 5.0.3 on 2024-05-22 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employeid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'manager'), ('sde', 'sde'), ('project lead', 'pl')], max_length=50)),
                ('companyy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
