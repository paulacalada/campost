# Generated by Django 4.1.2 on 2022-11-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    #dependencies = [
     #   ('client', '0001_initial'),
    #]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('prenom', models.CharField(max_length=70)),
                ('telephone', models.CharField(max_length=70)),
                ('adresse', models.CharField(max_length=70)),
            ],
        ),
    ]
