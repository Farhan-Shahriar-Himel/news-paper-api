# Generated by Django 5.0.2 on 2024-04-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleclass',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='Article/media/uploads'),
        ),
    ]
