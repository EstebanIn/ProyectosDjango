# Generated by Django 4.0.5 on 2022-06-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_maestrousuario_pwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestrousuario',
            name='pwd',
            field=models.CharField(max_length=50),
        ),
    ]
