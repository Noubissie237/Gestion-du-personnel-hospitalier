# Generated by Django 4.2.6 on 2023-12-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_consultation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='Date',
            field=models.DateField(),
        ),
    ]
