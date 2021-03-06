# Generated by Django 3.0.7 on 2020-08-22 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_ac_type', models.CharField(max_length=50, null=True, verbose_name='AC Type')),
                ('c_amount', models.FloatField(blank=True, null=True)),
                ('c_advance', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Cardemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.CharField(blank=True, max_length=50, null=True, verbose_name='car name')),
                ('img', models.ImageField(blank=True, null=True, upload_to='4wheeler/Images/', verbose_name='Car Image')),
                ('ac_price', models.FloatField(blank=True, null=True, verbose_name='Car Ac Price')),
                ('without_ac_price', models.FloatField(blank=True, null=True, verbose_name='Car Without Ac Price')),
                ('advance', models.CharField(blank=True, choices=[('25', '25'), ('50', '50'), ('75', '75'), ('100', '100')], max_length=50, null=True, verbose_name='Adavnce Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('airport_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Airport_name')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True, verbose_name='Gender')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone No.')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profile Image')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('p_Phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mobile Number')),
                ('p_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Demo@gmail.com')),
                ('p_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Exact Drop Location (Optional)')),
                ('p_order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('p_created_on', models.DateTimeField(auto_now_add=True)),
                ('P_updated_on', models.DateTimeField(auto_now=True)),
                ('p_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PersionInfo',
                'verbose_name_plural': 'PersionInfos',
            },
        ),
        migrations.CreateModel(
            name='OutStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_trip_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Trip Type')),
                ('os_from', models.CharField(blank=True, max_length=100, null=True, verbose_name='FROM city -e.g. Wankidi')),
                ('os_to', models.CharField(blank=True, max_length=100, null=True, verbose_name='TO city -e.g. Hyderabad')),
                ('os_pickup', models.DateField(blank=True, null=True, verbose_name='PICK UP')),
                ('os_return', models.DateField(blank=True, null=True, verbose_name='RETURN')),
                ('os_picktime', models.CharField(blank=True, max_length=100, null=True, verbose_name='PICK UP AT')),
                ('os_status', models.BooleanField(default=True)),
                ('os_created_on', models.DateTimeField(auto_now_add=True)),
                ('os_updated_on', models.DateTimeField(auto_now=True)),
                ('os_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.Car')),
                ('os_persional_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.PersionInfo')),
                ('os_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='os', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OutStation',
                'verbose_name_plural': 'OutStations',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_from', models.CharField(blank=True, max_length=100, null=True, verbose_name='From -e.g. Wankidi')),
                ('l_to', models.CharField(blank=True, max_length=100, null=True, verbose_name='To -e.g. Mancherial')),
                ('l_pickup', models.DateField(blank=True, null=True, verbose_name='PICK UP')),
                ('l_picktime', models.CharField(blank=True, max_length=100, null=True, verbose_name='PICK UP AT')),
                ('l_return', models.DateField(blank=True, null=True, verbose_name='RETURN')),
                ('status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('l_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.Car')),
                ('l_persional_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.PersionInfo')),
                ('l_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locals',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='c_car',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.Cardemo'),
        ),
        migrations.AddField(
            model_name='car',
            name='c_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AirPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Airport Address -e.g. (RGIA) Rajiv Gandhi International Airport')),
                ('ap_trip', models.CharField(blank=True, max_length=50, null=True, verbose_name='Trip Type')),
                ('ap_pic_add', models.CharField(blank=True, max_length=100, null=True, verbose_name='Your Address -e.g. Wankidi')),
                ('ap_pickup', models.DateField(blank=True, null=True, verbose_name='PICK UP')),
                ('ap_picktime', models.CharField(blank=True, max_length=100, null=True, verbose_name='PICK UP AT')),
                ('ap_return', models.DateField(blank=True, null=True, verbose_name='RETURN')),
                ('status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('ap_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.Car')),
                ('ap_persional_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.PersionInfo')),
                ('ap_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AirPort',
                'verbose_name_plural': 'AirPorts',
            },
        ),
    ]
