# Generated by Django 2.0.3 on 2018-12-13 01:50

from django.db import migrations
import util.fields
import util.time


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snake',
            name='created',
            field=util.fields.CreatedDateTimeField(blank=True, default=util.time.now, editable=False),
        ),
        migrations.AddField(
            model_name='snake',
            name='modified',
            field=util.fields.ModifiedDateTimeField(blank=True, default=util.time.now, editable=False),
        ),
        migrations.AddField(
            model_name='usersnake',
            name='created',
            field=util.fields.CreatedDateTimeField(blank=True, default=util.time.now, editable=False),
        ),
        migrations.AddField(
            model_name='usersnake',
            name='modified',
            field=util.fields.ModifiedDateTimeField(blank=True, default=util.time.now, editable=False),
        ),
    ]
