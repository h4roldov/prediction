# Generated by Django 2.2.4 on 2019-08-27 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='source',
            new_name='model_source',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='file_name',
        ),
    ]