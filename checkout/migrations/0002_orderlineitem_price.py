# Generated by Django 3.2.8 on 2021-11-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]