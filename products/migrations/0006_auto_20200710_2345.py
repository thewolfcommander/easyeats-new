# Generated by Django 3.0.4 on 2020-07-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_food_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantreview',
            name='rating_2',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='rating_3',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='rating_4',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='rating_5',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_2',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_3',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_4',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_5',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
    ]
