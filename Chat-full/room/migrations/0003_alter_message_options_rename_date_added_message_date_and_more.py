# Generated by Django 4.1.3 on 2023-01-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date',)},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date_added',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='value',
        ),
    ]
