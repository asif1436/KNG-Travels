# Generated by Django 3.0.7 on 2020-08-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0003_auto_20200820_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citys',
            name='city_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
    ]
