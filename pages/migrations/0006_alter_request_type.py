# Generated by Django 4.2.3 on 2023-07-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.CharField(choices=[('regular', 'معمولی'), ('instance', 'فوری')], max_length=50),
        ),
    ]
