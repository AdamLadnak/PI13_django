# Generated by Django 4.2.7 on 2024-04-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0005_student_obec_student_psc_student_ulica'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucitel',
            name='obec',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ucitel',
            name='psc',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='ucitel',
            name='ulica',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
