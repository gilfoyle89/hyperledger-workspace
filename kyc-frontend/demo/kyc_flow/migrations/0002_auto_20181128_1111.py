# Generated by Django 2.1.3 on 2018-11-28 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc_flow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycsubmitprocess',
            name='email',
            field=models.CharField(default='Please enter the value', max_length=150, verbose_name='E-Mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kycsubmitprocess',
            name='first_name',
            field=models.CharField(default='Please enter the value', max_length=150, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kycsubmitprocess',
            name='last_name',
            field=models.CharField(default='Please enter the value', max_length=150, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kycsubmitprocess',
            name='rejected',
            field=models.BooleanField(default=False, verbose_name='Reject'),
        ),
    ]
