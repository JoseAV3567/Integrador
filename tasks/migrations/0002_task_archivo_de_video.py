# Generated by Django 4.2.4 on 2023-10-05 01:16

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='archivo_de_video',
            field=models.FileField(default='default_video.mp4', upload_to='videos/', validators=[tasks.models.validate_file_size]),
            preserve_default=False,
        ),
    ]
