# Generated by Django 4.0.5 on 2022-06-26 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_websolicitudservicio_fechavisita_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webfactura',
            name='fechafac',
        ),
    ]
