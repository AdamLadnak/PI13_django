# Generated by Django 4.2.7 on 2024-04-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0009_alter_student_datum_narodenia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=20)),
                ('priezvisko', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('datum', models.DateField()),
            ],
            options={
                'verbose_name': 'Užívateľ',
                'verbose_name_plural': 'Užívatelia',
                'ordering': ['priezvisko', 'meno'],
            },
        ),
    ]
