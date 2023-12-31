# Generated by Django 4.2.6 on 2023-12-24 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_medecin_remove_patient_medecin_attitré_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='medecin',
            name='Specialite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.specialite'),
        ),
    ]
