# Generated by Django 2.0.1 on 2018-02-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180201_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='tamaño',
            field=models.CharField(blank=True, choices=[('P', 'Pequeño'), ('M', 'Medio'), ('G', 'Grande')], default='M', max_length=1),
        ),
    ]
