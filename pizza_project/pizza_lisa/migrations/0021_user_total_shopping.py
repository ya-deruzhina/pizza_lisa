# Generated by Django 5.0.1 on 2024-02-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_lisa', '0020_alter_catalogmodel_price_disсont'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_shopping',
            field=models.FloatField(default=0),
        ),
    ]
