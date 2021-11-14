# Generated by Django 3.2.7 on 2021-10-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='birthday',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='applicant',
            name='birthmonth',
            field=models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='applicant',
            name='birthyear',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='city',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Nonbinary'), ('other', 'Other')], default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='grade',
            field=models.CharField(choices=[(9, 'Freshman'), (10, 'Sophomore'), (11, 'Junior'), (12, 'Senior')], default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='school',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='state',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='street_address',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='zip_code',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
