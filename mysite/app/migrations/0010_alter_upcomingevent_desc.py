# Generated by Django 3.2.7 on 2021-11-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_upcomingevent_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevent',
            name='desc',
            field=models.CharField(default=None, max_length=600),
        ),
    ]