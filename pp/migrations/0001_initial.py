# Generated by Django 3.0.4 on 2020-03-10 07:57

from django.db import migrations, models
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('file', private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='File')),
            ],
        ),
    ]
