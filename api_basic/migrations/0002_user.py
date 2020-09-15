# Generated by Django 3.1.1 on 2020-09-13 13:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, default='', max_length=100)),
                ('l_name', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Exactly 10 digits allowed.Starting digit can be 6,7,8,9", regex='^[6-9]{1}[0-9]{9}$')])),
                ('address_1', models.CharField(blank=True, default='', max_length=250)),
                ('address_2', models.CharField(blank=True, default='', max_length=250)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('zip_code', models.CharField(blank=True, default='', max_length=20)),
                ('is_sheltown_verified', models.BooleanField(default=False)),
                ('user_image', models.ImageField(blank=True, default='default_user_image.jpg', null=True, upload_to='user_profile_image/')),
                ('usertype', models.CharField(blank=True, choices=[('Property Owner', 'Property Owner'), ('Service Provider', 'Service Provider'), ('User', 'User')], max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('identity_proof', models.FileField(blank=True, upload_to='identity_proof/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]