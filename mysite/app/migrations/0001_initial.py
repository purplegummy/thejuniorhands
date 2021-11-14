# Generated by Django 3.2.7 on 2021-09-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=15)),
                ('month', models.CharField(max_length=3)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
