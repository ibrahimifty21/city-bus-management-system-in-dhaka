# Generated by Django 3.2.8 on 2021-11-23 17:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_alter_announcement_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='message',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
