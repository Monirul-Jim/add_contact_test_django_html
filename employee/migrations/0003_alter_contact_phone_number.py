# Generated by Django 5.1.1 on 2024-09-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
