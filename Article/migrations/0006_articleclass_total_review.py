# Generated by Django 5.0.2 on 2024-06-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0005_userdetails_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleclass',
            name='total_review',
            field=models.IntegerField(default=0),
        ),
    ]
