# Generated by Django 4.1.4 on 2023-01-23 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.RenameField(
            model_name='amenity',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='amenity',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
