# Generated by Django 4.2.7 on 2024-04-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0007_student_datum_narodenia_student_rok_narodenia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucitel',
            name='datum_narodenia',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
