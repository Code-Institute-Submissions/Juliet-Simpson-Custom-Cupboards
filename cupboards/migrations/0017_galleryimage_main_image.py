# Generated by Django 3.2.8 on 2021-11-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupboards', '0016_alter_cupboard_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='main_image',
            field=models.BooleanField(default=False),
        ),
    ]
