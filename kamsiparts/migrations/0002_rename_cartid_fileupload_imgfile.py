# Generated by Django 4.1.1 on 2022-09-30 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kamsiparts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='cartId',
            new_name='imgFile',
        ),
    ]
