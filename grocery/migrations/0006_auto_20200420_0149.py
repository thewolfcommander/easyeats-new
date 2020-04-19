# Generated by Django 3.0.4 on 2020-04-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_grocery_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery',
            name='description',
        ),
        migrations.RemoveField(
            model_name='grocery',
            name='summary',
        ),
        migrations.AddField(
            model_name='grocery',
            name='quantity',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='grocery',
            name='scale',
            field=models.CharField(choices=[('gram', 'Gram'), ('kg', 'Kilogram')], default='kg', max_length=100),
        ),
    ]
