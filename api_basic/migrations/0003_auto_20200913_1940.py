# Generated by Django 3.1.1 on 2020-09-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
