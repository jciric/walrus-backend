# Generated by Django 2.2.2 on 2019-06-28 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190628_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
