# Generated by Django 4.1.3 on 2022-11-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='markscard',
            field=models.URLField(),
        ),
    ]