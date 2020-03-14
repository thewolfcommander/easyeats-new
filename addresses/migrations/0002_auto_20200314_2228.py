# Generated by Django 3.0.4 on 2020-03-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(choices=[('india', 'India')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='mobile_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('uttarakhand', 'Uttarakhand')], max_length=255, null=True),
        ),
    ]
