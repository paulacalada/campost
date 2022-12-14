# Generated by Django 4.1.2 on 2022-11-17 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_compte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client', verbose_name='Proprietaire du compte'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='jour',
            field=models.DateTimeField(null=True, verbose_name='jour'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='numero',
            field=models.CharField(max_length=70, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='solde',
            field=models.FloatField(default=0, verbose_name='Solde initial du compte'),
        ),
    ]
