# Generated by Django 5.0.1 on 2024-01-27 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_lisa', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pizza', models.CharField()),
                ('ingredients', models.TextField()),
                ('price', models.FloatField()),
                ('price_diskont', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_message', models.CharField(default='admin', max_length=100)),
                ('message', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('new', models.BooleanField(default=True)),
                ('user_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('COOKING', 'COOKING'), ('TASTING', 'TASTING'), ('PACKING', 'PACKING'), ('IN_DELIVERY', 'IN_DELIVERY'), ('ARCHIVE', 'ARCHIVE')], default='NEW')),
                ('count', models.IntegerField()),
                ('name', models.CharField()),
                ('phone', models.BigIntegerField()),
                ('comment', models.TextField(null=True)),
                ('name_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_lisa.catalog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_lisa.catalog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]