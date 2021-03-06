# Generated by Django 3.1.2 on 2020-10-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_owner_name', models.CharField(max_length=90, verbose_name='Propietario de la invitación')),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('telephone', models.CharField(max_length=16)),
                ('guest_names', models.CharField(max_length=256, verbose_name='Nombres de invitados')),
                ('number_of_guests', models.IntegerField(verbose_name='Total de invitados')),
                ('guests_confirmed', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nombres confirmados')),
                ('total_guests_confirmed', models.IntegerField(blank=True, null=True, verbose_name='Total de confirmados')),
                ('is_RSVP', models.BooleanField(blank=True, null=True, verbose_name='¿Confirmó?')),
                ('date_RSVP', models.DateField(blank=True, null=True, verbose_name='Fecha confirmación')),
            ],
            options={
                'verbose_name_plural': 'Invitaciones',
            },
        ),
    ]
