# Generated by Django 5.0.1 on 2024-01-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_lisa', '0003_user_discont_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]