# Generated by Django 5.0.1 on 2024-02-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_lisa', '0018_ordermodel_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='adress',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.TextField(default='Self-pickup'),
        ),
    ]
