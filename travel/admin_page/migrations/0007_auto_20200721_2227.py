# Generated by Django 3.0.7 on 2020-07-21 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_page', '0006_auto_20200721_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outstation',
            name='os_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='os', to=settings.AUTH_USER_MODEL),
        ),
    ]