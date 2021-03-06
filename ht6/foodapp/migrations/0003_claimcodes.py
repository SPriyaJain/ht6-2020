# Generated by Django 3.1 on 2020-08-23 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_foodprovider_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.foodprovider')),
            ],
        ),
    ]
