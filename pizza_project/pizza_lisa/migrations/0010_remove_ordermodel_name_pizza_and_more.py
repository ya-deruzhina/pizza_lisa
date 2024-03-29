# Generated by Django 5.0.1 on 2024-02-04 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_lisa', '0009_basketmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='name_pizza',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='order_time',
        ),
        migrations.CreateModel(
            name='PizzaInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_lisa.ordermodel')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_lisa.catalogmodel')),
            ],
        ),
    ]
