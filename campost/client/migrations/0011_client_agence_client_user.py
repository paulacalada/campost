# Generated by Django 4.1.3 on 2022-11-20 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0010_profil_connected_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='agence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.agence'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
