# Generated by Django 4.0.4 on 2022-04-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuit_id', models.CharField(max_length=100)),
                ('circuit_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
