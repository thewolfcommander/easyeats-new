# Generated by Django 3.0.4 on 2020-04-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_food_collection'),
        ('grocery', '0006_auto_20200420_0149'),
        ('cart', '0002_cart_groceries'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.Grocery')),
            ],
        ),
        migrations.CreateModel(
            name='FoodEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Food')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='foods',
            field=models.ManyToManyField(to='cart.FoodEntry'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='groceries',
            field=models.ManyToManyField(to='cart.GroceryEntry'),
        ),
    ]
