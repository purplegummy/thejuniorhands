# Generated by Django 3.2.7 on 2021-12-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0008_auto_20211121_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
