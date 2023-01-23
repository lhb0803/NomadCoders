# Generated by Django 4.1.4 on 2023-01-23 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('rooms', '0003_alter_amenity_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
