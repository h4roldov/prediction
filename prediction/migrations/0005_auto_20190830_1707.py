# Generated by Django 2.2.4 on 2019-08-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_auto_20190830_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='model_file',
            field=models.FileField(default='settings.MEDIA_ROOT/modelDT.file', upload_to='documents/'),
        ),
    ]